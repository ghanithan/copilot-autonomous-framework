#!/usr/bin/env python3
"""
GitHub Copilot Autonomous Development Framework
Configuration Generator

Generates: copilot-instructions.md, copilot-context.md, copilot-setup-steps.yml
           claude-context.md, .claude/commands/
"""
import os
import sys
import yaml
import argparse
import re
from pathlib import Path
from typing import Dict, Any, List, Union

class TemplateEngine:
    """Enhanced template engine with better variable substitution and control structures"""
    
    def __init__(self):
        self.context = {}
    
    def render(self, template_content: str, context: Dict[str, Any]) -> str:
        """Render template with context variables"""
        self.context = context
        result = template_content
        
        # Handle {{#each ARRAY}} loops
        result = self._handle_each_loops(result, context)
        
        # Handle {{#if CONDITION}} conditionals
        result = self._handle_conditionals(result, context)
        
        # Handle simple variable substitution {{VARIABLE}}
        result = self._substitute_variables(result, context)
        
        # Clean up any remaining template syntax
        result = self._cleanup_template_syntax(result)
        
        return result
    
    def _substitute_variables(self, content: str, context: Dict[str, Any]) -> str:
        """Handle simple variable substitution"""
        def replace_var(match):
            var_name = match.group(1).strip()
            return str(context.get(var_name, f"{{{{ {var_name} }}}}"))  # Keep unresolved vars
        
        return re.sub(r'\{\{([^#/][^}]*)\}\}', replace_var, content)
    
    def _handle_each_loops(self, content: str, context: Dict[str, Any]) -> str:
        """Handle {{#each ARRAY}} ... {{/each}} loops"""
        pattern = r'\{\{#each\s+(\w+)\}\}(.*?)\{\{/each\}\}'
        
        def replace_each(match):
            array_name = match.group(1)
            loop_content = match.group(2)
            
            if array_name not in context:
                return ""
            
            array_data = context[array_name]
            if not isinstance(array_data, list):
                return ""
            
            result_parts = []
            for item in array_data:
                item_content = loop_content
                
                if isinstance(item, dict):
                    # Replace properties with uppercase keys
                    for key, value in item.items():
                        item_content = item_content.replace(f"{{{{{key.upper()}}}}}", str(value))
                elif isinstance(item, str):
                    item_content = item_content.replace("{{this}}", item)
                
                result_parts.append(item_content)
            
            return "".join(result_parts)
        
        return re.sub(pattern, replace_each, content, flags=re.DOTALL)
    
    def _handle_conditionals(self, content: str, context: Dict[str, Any]) -> str:
        """Handle {{#if CONDITION}} ... {{/if}} conditionals"""
        pattern = r'\{\{#if\s+(\w+)\}\}(.*?)\{\{/if\}\}'
        
        def replace_if(match):
            condition_name = match.group(1)
            if_content = match.group(2)
            
            # Check if condition is truthy
            condition_value = context.get(condition_name, False)
            if condition_value:
                return if_content
            return ""
        
        return re.sub(pattern, replace_if, content, flags=re.DOTALL)
    
    def _cleanup_template_syntax(self, content: str) -> str:
        """Remove any remaining template syntax and clean up formatting"""
        # Remove {{#unless}} blocks (not implemented)
        content = re.sub(r'\{\{#unless.*?\}\}.*?\{\{/unless\}\}', '', content, flags=re.DOTALL)
        
        # Clean up extra whitespace but preserve intentional formatting
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content.strip()


class CopilotConfigGenerator:
    """Main configuration generator for GitHub Copilot autonomous development"""
    
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config = self.load_config(config_path)
        self.template_engine = TemplateEngine()
        self.base_dir = self.config_path.parent
        self.framework_dir = self.find_framework_directory()
        
    def find_framework_directory(self) -> Path:
        """Find the framework directory"""
        current_dir = Path(__file__).parent.parent
        if current_dir.name in ["copilot-autonomous-framework-standalone", "copilot-autonomous-framework"]:
            return current_dir
        
        # Try relative paths
        for path in [
            self.base_dir / "copilot-autonomous-framework-standalone",
            self.base_dir / "copilot-autonomous-framework", 
            self.base_dir.parent / "copilot-autonomous-framework-standalone",
            self.base_dir.parent / "copilot-autonomous-framework",
            Path("/Users/ghanithan/work/src/personal/copilot-autonomous-framework")  # Absolute fallback
        ]:
            if path.exists():
                return path
        
        raise FileNotFoundError("Could not find framework directory")
    
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load project configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def load_stack_configs(self) -> Dict[str, Any]:
        """Load technology stack configurations"""
        configs = {}
        
        # Load backend config
        if 'stack' in self.config and 'backend' in self.config['stack']:
            backend = self.config['stack']['backend']
            if 'config_ref' in backend:
                config_path = self.framework_dir / backend['config_ref']
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        backend_config = yaml.safe_load(f)
                        configs.update(backend_config)
        
        # Load frontend config
        if 'stack' in self.config and 'frontend' in self.config['stack']:
            frontend = self.config['stack']['frontend']
            if 'config_ref' in frontend:
                config_path = self.framework_dir / frontend['config_ref']
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        frontend_config = yaml.safe_load(f)
                        configs.update(frontend_config)
        
        return configs
    
    def prepare_template_context(self) -> Dict[str, Any]:
        """Prepare comprehensive context for template rendering"""
        stack_configs = self.load_stack_configs()
        context = {}
        
        # Flatten project configuration
        self._flatten_config_section(context, self.config, "")
        
        # Add stack detection flags
        stack = self.config.get('stack', {})
        backend_lang = stack.get('backend', {}).get('language', '')
        frontend_lang = stack.get('frontend', {}).get('language', '')
        
        context.update({
            'RUST_BACKEND': backend_lang == 'rust',
            'PYTHON_BACKEND': backend_lang == 'python', 
            'NODE_BACKEND': backend_lang in ['node', 'nodejs'],
            'REACT_FRONTEND': frontend_lang == 'typescript' and stack.get('frontend', {}).get('framework') == 'react',
            'VUE_FRONTEND': stack.get('frontend', {}).get('framework') == 'vue',
            'ANGULAR_FRONTEND': stack.get('frontend', {}).get('framework') == 'angular',
            'NODE_FRONTEND': frontend_lang in ['javascript', 'typescript']
        })
        
        # Add stack configurations
        context.update(stack_configs)
        
        # Handle special formatting for arrays and complex structures
        self._format_special_fields(context)
        
        return context
    
    def _flatten_config_section(self, context: Dict[str, Any], section: Dict[str, Any], prefix: str):
        """Recursively flatten configuration sections"""
        for key, value in section.items():
            context_key = f"{prefix}_{key}".upper() if prefix else key.upper()
            
            if isinstance(value, dict) and key not in ['stack', 'timeline', 'users']:
                # Don't flatten certain complex sections
                self._flatten_config_section(context, value, context_key)
            else:
                context[context_key] = value
    
    def _format_special_fields(self, context: Dict[str, Any]):
        """Format special fields for template rendering"""
        # Format principles as comma-separated string
        if 'ARCHITECTURE' in context and 'PRINCIPLES' in context['ARCHITECTURE']:
            principles = context['ARCHITECTURE']['PRINCIPLES']
            if isinstance(principles, list):
                context['PRINCIPLES'] = ', '.join(principles)
        
        # Ensure arrays are available for iteration
        for key in ['TARGET_USERS', 'VALUE_PROPOSITIONS', 'TIMELINE_PHASES', 'PERFORMANCE_TARGETS']:
            if key not in context:
                context[key] = []
        
        # Set default values for common template variables
        defaults = {
            'TEST_COVERAGE': context.get('QUALITY', {}).get('test_coverage_threshold', 90),
            'ARCHITECTURE_PATTERN': context.get('ARCHITECTURE', {}).get('pattern', 'clean-architecture'),
            'COMPONENT_TYPE': 'struct/function' if context.get('RUST_BACKEND') else 'class/function',
            'INTERFACE_PATTERN': 'traits' if context.get('RUST_BACKEND') else 'interfaces',
            'PRIMARY_LANGUAGE': context.get('STACK', {}).get('backend', {}).get('language', 'rust')
        }
        
        for key, default_value in defaults.items():
            if key not in context:
                context[key] = default_value
    
    def load_template(self, template_name: str) -> str:
        """Load template file from framework"""
        template_path = self.framework_dir / "templates" / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        
        with open(template_path, 'r') as f:
            return f.read()
    
    def generate_copilot_instructions(self) -> str:
        """Generate .github/copilot-instructions.md"""
        template = self.load_template('copilot-instructions.template.md')
        context = self.prepare_template_context()
        return self.template_engine.render(template, context)
    
    def generate_copilot_context(self) -> str:
        """Generate .github/copilot-context.md"""
        template = self.load_template('copilot-context.template.md')
        context = self.prepare_template_context()
        return self.template_engine.render(template, context)
    
    def generate_setup_steps(self) -> str:
        """Generate .github/copilot-setup-steps.yml"""
        template = self.load_template('copilot-setup-steps.template.yml')
        context = self.prepare_template_context()
        return self.template_engine.render(template, context)
    
    def generate_claude_context(self) -> str:
        """Generate CLAUDE.md for Claude GitHub app integration"""
        template = self.load_template('claude-context.template.md')
        context = self.prepare_template_context()
        return self.template_engine.render(template, context)
    
    def generate_claude_commands(self, output_dir: str = '.'):
        """Generate .claude/commands/ directory with custom review commands"""
        output_path = Path(output_dir)
        claude_commands_dir = output_path / '.claude' / 'commands'
        claude_commands_dir.mkdir(parents=True, exist_ok=True)
        
        # Get list of command templates
        commands_dir = self.framework_dir / 'templates' / 'claude-commands'
        if not commands_dir.exists():
            print("⚠️  Claude commands templates not found, skipping...")
            return
        
        context = self.prepare_template_context()
        
        # Copy command files
        for command_file in commands_dir.glob('*.md'):
            if command_file.name == 'README.md':
                continue  # Skip README for now, will process separately
                
            template_content = command_file.read_text()
            rendered_content = self.template_engine.render(template_content, context)
            
            output_file = claude_commands_dir / command_file.name
            output_file.write_text(rendered_content)
            print(f"📝 Generated Claude command: {output_file}")
        
        # Generate README for commands
        readme_path = commands_dir / 'README.md'
        if readme_path.exists():
            readme_content = readme_path.read_text()
            rendered_readme = self.template_engine.render(readme_content, context)
            (claude_commands_dir / 'README.md').write_text(rendered_readme)
            print(f"📚 Generated Claude commands README: {claude_commands_dir / 'README.md'}")
    
    def generate_issue_template(self, output_dir: str = '.'):
        """Generate GitHub issue template"""
        template = self.load_template('github-issue-template.md')
        context = self.prepare_template_context()
        
        # Add template-specific context
        context.update({
            'PRD_DOCUMENT_PATH': context.get('PRD_REFERENCE', 'docs/prd.md'),
            'TECHNICAL_SPEC_PATH': context.get('TECHNICAL_SPEC_REFERENCE', 'docs/technical-spec.md'),
            'ARCHITECTURE_LAYERS_OPTIONS': 'entities/use_cases/adapters/frameworks',
            'PERFORMANCE_TARGET_EXAMPLE': '50ms for complex operations',
            'MEMORY_TARGET_EXAMPLE': '<1MB allocations',
            'BENCHMARK_COMMAND_EXAMPLE': 'cargo bench --bench feature_name',
            'EXAMPLE_SOURCE_PATH': 'src/feature',
            'EXAMPLE_TEST_PATH': 'tests/feature',
            'EXAMPLE_BENCH_PATH': 'benches/feature',
            'BUILD_COMMAND': 'cargo check' if context.get('RUST_BACKEND') else 'npm run build',
            'TEST_COMMAND': 'cargo test' if context.get('RUST_BACKEND') else 'npm test',
            'BENCHMARK_COMMAND': 'cargo bench' if context.get('RUST_BACKEND') else 'npm run bench',
            'COVERAGE_COMMAND': 'cargo tarpaulin' if context.get('RUST_BACKEND') else 'npm run coverage',
            'FORMAT_COMMAND': 'cargo fmt' if context.get('RUST_BACKEND') else 'npm run format',
            'LINT_COMMAND': 'cargo clippy' if context.get('RUST_BACKEND') else 'npm run lint',
            'ARCHITECTURE_VALIDATION_COMMAND': 'python scripts/validate-architecture.py'
        })
        
        rendered = self.template_engine.render(template, context)
        
        # Write to issue template directory
        output_path = Path(output_dir)
        issue_template_dir = output_path / '.github' / 'ISSUE_TEMPLATE'
        issue_template_dir.mkdir(parents=True, exist_ok=True)
        
        (issue_template_dir / 'copilot-autonomous-task.md').write_text(rendered)
        print(f"📋 Generated GitHub issue template at {issue_template_dir / 'copilot-autonomous-task.md'}")
    
    def generate_all_configs(self, output_dir: str = '.'):
        """Generate all GitHub Copilot and Claude configuration files"""
        output_path = Path(output_dir)
        github_dir = output_path / '.github'
        github_dir.mkdir(exist_ok=True)
        
        print(f"🚀 Generating GitHub Copilot + Claude configuration for {self.config['project']['name']}...")
        
        try:
            # Generate core Copilot files
            print("📝 Generating copilot-instructions.md...")
            instructions = self.generate_copilot_instructions()
            (github_dir / 'copilot-instructions.md').write_text(instructions)
            
            print("📋 Generating copilot-context.md...")
            context = self.generate_copilot_context()
            (github_dir / 'copilot-context.md').write_text(context)
            
            print("⚙️  Generating copilot-setup-steps.yml...")
            setup_steps = self.generate_setup_steps()
            (github_dir / 'copilot-setup-steps.yml').write_text(setup_steps)
            
            # Generate Claude integration files
            print("🤖 Generating CLAUDE.md...")
            claude_context = self.generate_claude_context()
            (output_path / 'CLAUDE.md').write_text(claude_context)
            
            print("🔧 Generating Claude custom commands...")
            self.generate_claude_commands(output_dir)
            
            # Generate issue template
            print("🎫 Generating GitHub issue template...")
            self.generate_issue_template(output_dir)
            
            print("✅ Successfully generated GitHub Copilot + Claude configuration:")
            print("   - .github/copilot-instructions.md")
            print("   - .github/copilot-context.md")
            print("   - .github/copilot-setup-steps.yml")
            print("   - .github/ISSUE_TEMPLATE/copilot-autonomous-task.md")
            print("   - CLAUDE.md")
            print("   - .claude/commands/ (review commands)")
            
            # Validate generated files
            self.validate_generated_files(github_dir)
            
        except Exception as e:
            print(f"❌ Error generating configuration: {e}")
            raise
    
    def validate_generated_files(self, github_dir: Path):
        """Validate that generated files are well-formed"""
        required_files = [
            'copilot-instructions.md',
            'copilot-context.md',
            'copilot-setup-steps.yml'
        ]
        
        for filename in required_files:
            filepath = github_dir / filename
            if not filepath.exists():
                raise FileNotFoundError(f"Failed to generate {filename}")
            
            if filepath.stat().st_size == 0:
                raise ValueError(f"Generated {filename} is empty")
        
        # Validate YAML syntax
        try:
            with open(github_dir / 'copilot-setup-steps.yml', 'r') as f:
                yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Generated copilot-setup-steps.yml has invalid YAML: {e}")
        
        print("✅ All generated files validated successfully")


def main():
    parser = argparse.ArgumentParser(description='Generate GitHub Copilot autonomous development configuration')
    parser.add_argument('config', nargs='?', default='project-config.yml',
                       help='Project configuration file (default: project-config.yml)')
    parser.add_argument('--output', '-o', default='.', 
                       help='Output directory (default: current directory)')
    parser.add_argument('--validate', action='store_true',
                       help='Only validate configuration without generating files')
    parser.add_argument('--issue-template-only', action='store_true',
                       help='Generate only the GitHub issue template')
    parser.add_argument('--claude-only', action='store_true',
                       help='Generate only Claude integration files (CLAUDE.md and commands)')
    parser.add_argument('--copilot-only', action='store_true',
                       help='Generate only GitHub Copilot files (no Claude integration)')
    
    args = parser.parse_args()
    
    if not Path(args.config).exists():
        print(f"❌ Configuration file not found: {args.config}")
        print(f"💡 Create {args.config} based on examples or specify a different config file")
        sys.exit(1)
    
    try:
        generator = CopilotConfigGenerator(args.config)
        
        if args.validate:
            print("✅ Configuration file is valid")
        elif args.issue_template_only:
            generator.generate_issue_template(args.output)
        elif args.claude_only:
            print(f"🤖 Generating Claude integration files for {generator.config['project']['name']}...")
            output_path = Path(args.output)
            
            claude_context = generator.generate_claude_context()
            (output_path / 'CLAUDE.md').write_text(claude_context)
            print("✅ Generated CLAUDE.md")
            
            generator.generate_claude_commands(args.output)
            print("✅ Generated Claude custom commands")
        elif args.copilot_only:
            print(f"🚀 Generating GitHub Copilot files for {generator.config['project']['name']}...")
            output_path = Path(args.output)
            github_dir = output_path / '.github'
            github_dir.mkdir(exist_ok=True)
            
            instructions = generator.generate_copilot_instructions()
            (github_dir / 'copilot-instructions.md').write_text(instructions)
            
            context = generator.generate_copilot_context()
            (github_dir / 'copilot-context.md').write_text(context)
            
            setup_steps = generator.generate_setup_steps()
            (github_dir / 'copilot-setup-steps.yml').write_text(setup_steps)
            
            generator.generate_issue_template(args.output)
            
            print("✅ Generated GitHub Copilot configuration (Copilot only)")
        else:
            generator.generate_all_configs(args.output)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()