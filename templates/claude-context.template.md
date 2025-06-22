# {{PROJECT_NAME}} - Claude Code Review Context

## Project Overview

**Mission**: {{PROJECT_MISSION}}
**Description**: {{PROJECT_DESCRIPTION}}
**Domain**: {{DOMAIN_CONTEXT}}

## Architecture & Design Principles

### Clean Architecture Layers
- **Entities**: {{#each ENTITY_EXAMPLES}}
  - **{{name}}**: {{description}}{{/each}}

- **Use Cases**: {{#each USE_CASE_EXAMPLES}}
  - **{{name}}**: {{description}}{{/each}}

- **Adapters**: {{#each ADAPTER_EXAMPLES}}
  - **{{name}}**: {{description}}{{/each}}

- **Frameworks**: {{#each FRAMEWORK_EXAMPLES}}
  - **{{name}}**: {{description}}{{/each}}

### Design Principles
- **SOLID Principles**: Single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **Clean Architecture**: Dependency rule - dependencies point inward only
- **KISS**: Keep implementations simple and clear
- **YAGNI**: Only implement what's needed now
- **DRY**: Centralize repeated logic

## Technology Stack

### Backend
- **Language**: {{BACKEND_LANGUAGE}}
- **Framework**: {{BACKEND_FRAMEWORK}}
{{#if RUST_BACKEND}}
- **Error Handling**: Use `anyhow` for applications, `thiserror` for libraries
- **Async**: Prefer `tokio` async runtime with proper error propagation
- **Serialization**: All structs MUST have both JSON and YAML tags
{{/if}}
{{#if PYTHON_BACKEND}}
- **Type Hints**: Mandatory for all function signatures and class attributes
- **Error Handling**: Use custom exceptions for business logic errors
- **Async**: Use `asyncio` with proper error handling and resource cleanup
{{/if}}

### Frontend
- **Language**: {{FRONTEND_LANGUAGE}}
- **Framework**: {{FRONTEND_FRAMEWORK}}
{{#if REACT_FRONTEND}}
- **State Management**: Use Zustand for application state
- **Components**: Functional components with TypeScript interfaces
- **Testing**: Vitest for unit tests, Playwright for e2e tests
{{/if}}

## Performance Requirements

{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: {{TARGET}} ({{CONTEXT}})
{{/each}}

## Code Review Standards

### Architecture Compliance
1. **Dependency Rule**: Verify no inner layers depend on outer layers
2. **Interface Segregation**: Check interfaces are focused and minimal
3. **Single Responsibility**: Each module/class has one clear purpose
4. **Abstraction Levels**: Consistent abstraction within each layer

### Code Quality Metrics
- **Test Coverage**: Minimum {{TEST_COVERAGE_THRESHOLD}}%
- **Cyclomatic Complexity**: Maximum 10 per function
- **Function Length**: Maximum 50 lines per function
- **Class Size**: Maximum 200 lines per class

### Security Requirements
{{#if RUST_BACKEND}}
- No `unsafe` blocks without explicit justification
- Proper input validation using type system
- Secure error handling without information leakage
{{/if}}
{{#if PYTHON_BACKEND}}
- Input sanitization for all external data
- Proper exception handling without stack trace exposure
- SQL injection prevention using parameterized queries
{{/if}}

### Performance Standards
{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: Code must meet {{TARGET}} requirement
{{/each}}

## Domain-Specific Context

{{DOMAIN_CONTEXT}}

### Key Business Rules
{{#each BUSINESS_RULES}}
- {{rule}}: {{description}}
{{/each}}

### Integration Requirements
{{#each INTEGRATIONS}}
- **{{name}}**: {{purpose}}
  - API: {{api_details}}
{{/each}}

## Review Focus Areas

### 1. Architecture Review
- Clean Architecture layer separation
- Dependency rule compliance
- Interface design and abstraction
- Module cohesion and coupling

### 2. Performance Review
- Algorithm efficiency and complexity
- Resource usage (memory, CPU, I/O)
- Caching strategies and data access patterns
- Concurrent processing and async handling

### 3. Security Review
- Input validation and sanitization
- Authentication and authorization
- Data protection and encryption
- Error handling and information disclosure

### 4. Testing Review
- Test coverage and quality
- Unit test isolation and mocking
- Integration test scenarios
- Performance and load testing

### 5. Integration Review
- API design and versioning
- Error handling and retry logic
- Data consistency and transactions
- External service integration patterns

## Success Criteria

### Code Quality Gates
- All tests pass with {{TEST_COVERAGE_THRESHOLD}}% coverage
- No critical security vulnerabilities
- Performance benchmarks met
- Architecture compliance validated

### Documentation Requirements
- API endpoints documented with examples
- Complex algorithms explained with comments
- Architecture decisions recorded
- Performance characteristics documented

## Common Issues to Flag

### Architecture Violations
- Direct database access from use cases
- Business logic in controllers
- Framework dependencies in entities
- Circular dependencies between layers

### Performance Anti-Patterns
- N+1 database queries
- Blocking I/O in async contexts
- Memory leaks and resource cleanup
- Inefficient data structures

### Security Concerns
- Hardcoded secrets or credentials
- Unvalidated user input
- Improper error handling
- Missing authentication/authorization

## Review Workflow Integration

This context is designed to work with GitHub Copilot autonomous development:

1. **Copilot Implementation**: Copilot generates code following copilot-instructions.md
2. **Claude Review**: Claude reviews code using this context via custom commands
3. **Feedback Loop**: Claude provides structured feedback for Copilot improvements
4. **Quality Assurance**: Ensures both AI systems maintain consistent standards

Use custom commands in `.claude/commands/` for specialized review types that leverage this context.