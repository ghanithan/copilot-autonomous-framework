# GitHub Copilot Autonomous Development Framework

A comprehensive, configurable framework that enables GitHub Copilot to autonomously implement PRDs while maintaining KISS, YAGNI, SOLID, and Clean Architecture principles.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Overview

This framework generates the complete set of GitHub Copilot and Claude configuration files needed for autonomous development:

- **`.github/copilot-instructions.md`** - Main development instructions and coding standards
- **`.github/copilot-context.md`** - Project context and domain knowledge  
- **`.github/copilot-setup-steps.yml`** - Environment setup automation
- **`.github/ISSUE_TEMPLATE/copilot-autonomous-task.md`** - Issue template for autonomous tasks
- **`CLAUDE.md`** - Claude review context and project understanding
- **`.claude/commands/`** - Custom Claude review commands for specialized analysis

## ✨ Features

- **🏗️ Technology Stack Agnostic**: Supports Rust, Python, TypeScript/React, Vue.js, Angular, and more
- **🎯 Clean Architecture Enforcement**: Built-in validation of architectural principles
- **⚡ Performance-Driven**: Includes performance requirements and benchmarking
- **🔧 Template-Based**: Fully configurable through YAML configuration
- **♻️ Reusable**: Same framework works across different projects and PRDs
- **📊 Quality Assurance**: Automated testing, coverage, and compliance validation
- **🤖 Claude Integration**: Direct Claude GitHub app integration for comprehensive code reviews

## 🚀 Quick Start

### 1. Clone the Framework

```bash
git clone https://github.com/yourusername/copilot-autonomous-framework.git
cd copilot-autonomous-framework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Project

Choose an example configuration or create your own:

```bash
# Copy an example configuration
cp examples/jamstack-builder.yml my-project-config.yml

# Or copy the template for a custom configuration
cp templates/project-config.template.yml my-project-config.yml
```

Edit `my-project-config.yml` with your project details:

```yaml
project:
  name: "Your Project Name"
  description: "Your project description"
  mission: "Your project mission"

documents:
  prd_reference: "path/to/your/prd.md"
  technical_spec_reference: "path/to/your/technical-spec.md"

stack:
  backend:
    language: "rust"  # or "python", "node"
    framework: "tauri"  # or "fastapi", "express"
    config_ref: "configs/rust-backend.yml"
  frontend:
    language: "typescript"
    framework: "react"  # or "vue", "angular"
    config_ref: "configs/react-frontend.yml"
```

### 4. Generate Copilot Configuration

```bash
python generators/generate-copilot-config.py my-project-config.yml --output /path/to/your/project
```

This generates in your project directory:
- `.github/copilot-instructions.md`
- `.github/copilot-context.md`
- `.github/copilot-setup-steps.yml`
- `.github/ISSUE_TEMPLATE/copilot-autonomous-task.md`

### 5. Start Autonomous Development

With the generated configuration, GitHub Copilot can now:
- ✅ Understand your project context and requirements
- ✅ Follow your architectural principles automatically  
- ✅ Implement features according to your coding standards
- ✅ Meet performance requirements and quality gates

## 📁 Framework Structure

```
copilot-autonomous-framework/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── templates/
│   ├── copilot-instructions.template.md    # Main instructions template
│   ├── copilot-context.template.md         # Project context template
│   ├── copilot-setup-steps.template.yml    # Environment setup template
│   └── github-issue-template.md            # GitHub issue template
├── generators/
│   └── generate-copilot-config.py          # Main generator script
├── configs/
│   ├── rust-backend.yml                    # Rust/Tauri configuration
│   ├── python-backend.yml                  # Python/FastAPI configuration
│   └── react-frontend.yml                  # React/TypeScript configuration
├── examples/
│   ├── ecommerce-platform.yml             # E-commerce platform
│   └── saas-dashboard.yml                  # SaaS analytics dashboard
└── docs/
    └── getting-started.md                  # Detailed getting started guide
```

## 🛠️ Supported Technology Stacks

### Backend Technologies
- **Rust + Tauri**: High-performance desktop applications
- **Python + FastAPI**: Modern async API development
- **Node.js + Express**: Traditional web applications

### Frontend Technologies  
- **React + TypeScript**: Modern component-based UIs
- **Vue.js + TypeScript**: Progressive framework applications
- **Angular + TypeScript**: Enterprise-scale applications

### Architecture Patterns
- **Clean Architecture**: Dependency rule enforcement with proper layer separation
- **SOLID Principles**: Single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **KISS & YAGNI**: Keep it simple, implement only what's needed

## 📋 Example Configurations

### E-commerce Platform
Complete configuration for a modern e-commerce platform with:
- Rust backend with high-performance API
- Product catalog with search and filtering
- Shopping cart and checkout flow
- Payment processing with Stripe integration

```bash
cp examples/ecommerce-platform.yml my-config.yml
python generators/generate-copilot-config.py my-config.yml
```

### SaaS Analytics Dashboard
Configuration for a modern SaaS platform with:
- Python FastAPI backend with async operations
- React dashboard with real-time data visualization
- Multi-tenant architecture with user management
- PostgreSQL database with complex analytics

```bash
cp examples/saas-dashboard.yml my-config.yml
python generators/generate-copilot-config.py my-config.yml
```

## 🎯 Creating GitHub Issues for Copilot

After generating the configuration, you can create issues optimized for Copilot autonomous development:

1. **Use the Generated Issue Template**: The framework creates `.github/ISSUE_TEMPLATE/copilot-autonomous-task.md`

2. **Follow Copilot Best Practices**:
   - Clear, specific problem description
   - Detailed acceptance criteria with checkboxes
   - Explicit file list to create/modify
   - Architecture requirements and constraints
   - Performance targets and validation steps

3. **Reference Generated Context**: Issues should reference:
   - `.github/copilot-instructions.md` for coding standards
   - `.github/copilot-context.md` for project context
   - `.github/copilot-setup-steps.yml` for environment setup

## 🏗️ Architecture Validation

The framework includes automated validation for:

- **Clean Architecture Compliance**: Dependency rules enforcement
- **Performance Benchmarks**: Automated performance testing
- **Code Quality**: Linting and formatting standards
- **Test Coverage**: Minimum coverage requirements
- **Documentation**: API documentation completeness

Example validation commands generated for Rust projects:

```bash
# Architecture and quality validation
cargo check && cargo test && cargo bench
cargo tarpaulin --out Xml  # Test coverage
cargo fmt && cargo clippy -- -D warnings  # Code quality
python scripts/validate-architecture.py  # Architecture compliance
```

## 🔧 Customization

### Adding New Technology Stacks

1. Create a new configuration file in `configs/`:

```yaml
# configs/your-stack.yml
backend:
  language: "your-language"
  framework: "your-framework"
conventions:
  # Coding conventions specific to your stack
dependencies:
  # Required dependencies
language_conventions:
  # List of conventions for the issue template
```

2. Reference it in your project configuration:

```yaml
stack:
  backend:
    language: "your-language"
    framework: "your-framework"
    config_ref: "configs/your-stack.yml"
```

### Modifying Templates

All templates in the `templates/` directory use a simple variable substitution system:

- `{{VARIABLE_NAME}}` - Simple variable substitution
- `{{#if CONDITION}}...{{/if}}` - Conditional blocks
- `{{#each ARRAY}}...{{/each}}` - Array iteration

## 📊 Success Metrics

### Framework Validation
- ✅ All required GitHub Copilot files generated
- ✅ YAML syntax validation passed
- ✅ Template variable substitution working  
- ✅ Architecture compliance enforced
- ✅ Performance benchmarks defined

### Autonomous Development Benefits
- 🚀 **Rapid Setup**: Minutes instead of hours to configure Copilot
- 🎯 **Consistent Quality**: Same architectural standards across projects
- 📈 **Proven Patterns**: Battle-tested with real project implementations
- 🔧 **Extensible**: Easy to add new technology stacks and patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add your technology stack configuration or example
4. Test with a real project configuration
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Contributing Guidelines

- **New Technology Stacks**: Add configuration files in `configs/` with corresponding example in `examples/`
- **Template Improvements**: Enhance templates while maintaining backward compatibility
- **Documentation**: Update docs for any new features or configurations
- **Testing**: Test configurations with real projects before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by GitHub Copilot's autonomous development capabilities
- Built on Clean Architecture principles by Uncle Bob Martin
- Designed for modern development workflows and quality standards

---

**Ready to revolutionize your development workflow?** Generate your Copilot configuration and experience autonomous development that maintains the same quality standards as experienced developers! 🚀