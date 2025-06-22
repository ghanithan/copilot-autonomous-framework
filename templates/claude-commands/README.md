# Claude Custom Commands for Code Review

This directory contains specialized review commands that can be used with Claude GitHub app integration to provide comprehensive code review capabilities.

## Available Commands

### `/review-architecture`
**Purpose**: Review code for Clean Architecture compliance and design principles
- Validates Clean Architecture layer separation
- Checks SOLID principles adherence
- Identifies design pattern usage
- Flags architecture violations

### `/review-performance`
**Purpose**: Analyze performance characteristics and optimization opportunities
- Algorithm efficiency analysis
- Resource usage optimization
- Concurrency pattern validation
- Performance benchmark compliance

### `/review-security`
**Purpose**: Security vulnerability assessment and best practices validation
- Input validation and sanitization
- Authentication and authorization checks
- Data protection compliance
- Cryptography usage validation

### `/review-testing`
**Purpose**: Test coverage and quality assessment
- Coverage analysis and gaps identification
- Test quality and structure review
- Testing strategy validation
- Performance test verification

### `/review-integration`
**Purpose**: API design and external service integration review
- RESTful API design validation
- Error handling and resilience patterns
- Data consistency and transaction management
- Service communication security

## Usage with GitHub Copilot

### Workflow Integration
1. **Copilot generates code** following copilot-instructions.md
2. **Code review triggered** using Claude custom commands
3. **Claude provides feedback** based on project context in CLAUDE.md
4. **Iterative improvement** through AI collaboration

### Command Usage Examples

```markdown
# In GitHub PR or issue comments
@claude /review-architecture

# For specific areas of concern
@claude /review-performance - focus on database query optimization

# Multiple reviews
@claude /review-security
@claude /review-testing
```

### Context-Aware Reviews
Each command leverages project-specific context from:
- **CLAUDE.md**: Project domain, architecture, and requirements
- **Performance targets**: Specific benchmarks and SLA requirements
- **Technology stack**: Language and framework specific patterns
- **Integration requirements**: External service and API specifications

## Command Structure

Each command follows a consistent structure:

### Review Criteria
- Specific checkpoints for the review type
- Technology-specific considerations
- Common anti-patterns to identify

### Output Format
- Structured markdown review results
- Actionable recommendations with examples
- Scoring system for objective assessment

### Context Integration
- Project-specific requirements from CLAUDE.md
- Technology stack considerations
- Domain-specific validation rules

## Customization

### Adding New Commands
1. Create new `.md` file in this directory
2. Follow the established command structure
3. Reference project context variables from CLAUDE.md
4. Update this README with command description

### Modifying Existing Commands
- Commands use template variables from project configuration
- Customize review criteria based on project requirements
- Adjust scoring and validation rules as needed

## Integration with Autonomous Framework

These commands are designed to work seamlessly with the copilot-autonomous-framework:

### Generated Context
- Commands use variables populated by the framework generator
- Project-specific requirements automatically included
- Technology stack patterns pre-configured

### Quality Assurance
- Ensures consistent review standards across projects
- Maintains alignment with Clean Architecture principles
- Validates performance and security requirements

### Continuous Improvement
- Review feedback informs future Copilot implementations
- Creates learning loop between AI systems
- Maintains high code quality standards

## Best Practices

### When to Use Each Command
- **Architecture**: Major feature implementations, refactoring
- **Performance**: Critical path changes, optimization work
- **Security**: Authentication, data handling, API endpoints
- **Testing**: New feature completion, bug fixes
- **Integration**: External service changes, API modifications

### Review Frequency
- Run appropriate reviews for each PR
- Focus on specific commands based on change type
- Use multiple commands for complex changes

### Feedback Integration
- Address review feedback before merging
- Use feedback to improve Copilot instructions
- Update project context based on lessons learned

This command system enables comprehensive, context-aware code reviews that maintain high quality standards while supporting autonomous development workflows.