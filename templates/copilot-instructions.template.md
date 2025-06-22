# {{PROJECT_NAME}} Development Instructions

## Project Context
{{PROJECT_DESCRIPTION}}

Reference documents: {{PRD_REFERENCE}}{{#if TECHNICAL_SPEC_REFERENCE}}, {{TECHNICAL_SPEC_REFERENCE}}{{/if}}

## Architecture & Design Principles
We follow {{ARCHITECTURE_PATTERN}} with strict dependency rules - inner layers never depend on outer layers. Always implement entities, then use cases, then interface adapters, then frameworks.

We apply {{PRINCIPLES}} principles rigorously - each {{COMPONENT_TYPE}} has single responsibility, code is open for extension but closed for modification, and we depend on abstractions not concretions.

We practice KISS and YAGNI - implement only what's needed now, keep solutions simple, avoid premature optimization.

{{#if RUST_BACKEND}}
## Rust Conventions
All structs MUST have both JSON and YAML tags - this is non-negotiable for serialization compatibility.

Use anyhow for error handling in applications, thiserror for library errors. Always wrap errors with context using fmt::Errorf.

File naming uses snake_case ({{EXAMPLE_FILENAME}}.rs), functions use camelCase for private and PascalCase for public.

Constructor pattern: New functions should return interfaces when possible, use NewTypeName pattern.
{{/if}}

{{#if PYTHON_BACKEND}}
## Python Conventions
Follow PEP 8 style guide strictly. Use type hints for all function signatures.

Error handling with custom exception classes inheriting from base exceptions.

Use dataclasses or Pydantic models for structured data with validation.

File naming uses snake_case, class names use PascalCase, functions and variables use snake_case.
{{/if}}

{{#if NODE_BACKEND}}
## Node.js/TypeScript Conventions
Use strict TypeScript configuration with no implicit any.

Error handling with custom Error classes and proper error chaining.

File naming uses kebab-case, class names use PascalCase, functions and variables use camelCase.

Use async/await over promises, prefer immutable data structures.
{{/if}}

{{#if REACT_FRONTEND}}
## React/TypeScript Conventions
Component naming uses PascalCase, file naming uses kebab-case.

State management with {{STATE_MANAGEMENT}}, styling with {{STYLING_FRAMEWORK}}.

All props interfaces must be explicitly typed, use strict TypeScript configuration.

Custom hooks for business logic, prefer composition over inheritance.
{{/if}}

{{#if VUE_FRONTEND}}
## Vue.js/TypeScript Conventions
Component naming uses PascalCase, file naming uses kebab-case.

Use Composition API with TypeScript, avoid Options API for new components.

State management with {{STATE_MANAGEMENT}}, styling with {{STYLING_FRAMEWORK}}.
{{/if}}

{{#if ANGULAR_FRONTEND}}
## Angular/TypeScript Conventions
Follow Angular style guide strictly. Use reactive forms over template-driven forms.

Services for business logic, components for presentation only.

Use OnPush change detection strategy for performance.
{{/if}}

## Performance Requirements
{{#each PERFORMANCE_TARGETS}}
{{METRIC}} must complete in {{TARGET}} for {{CONTEXT}}.
{{/each}}

Use {{PARSING_STRATEGY}} for optimal parsing performance. Implement caching strategies to avoid redundant processing.

## Testing Standards
Every module requires comprehensive unit tests with >{{TEST_COVERAGE}}% coverage. Integration tests must validate cross-module interactions.

Performance benchmarks are mandatory - implement {{BENCHMARK_FRAMEWORK}}-based benchmarks for core operations.

## {{PROJECT_DOMAIN}} Specifics
{{PROJECT_DOMAIN_CONTEXT}}

{{#if CUSTOM_FEATURES}}
{{#each CUSTOM_FEATURES}}
{{FEATURE_NAME}}: {{FEATURE_DESCRIPTION}}
{{/each}}
{{/if}}

## Module Implementation Order
{{#each TIMELINE_PHASES}}
**{{NAME}}** (Days {{DAYS}}): {{DESCRIPTION}}
- Modules: {{MODULES}}
{{/each}}

## Error Handling Patterns
{{ERROR_HANDLING_PATTERN}}

Always provide meaningful error messages with context. Use structured error types with proper error chaining.

## Documentation Requirements
Every public function/{{COMPONENT_TYPE}}/interface requires comprehensive documentation with examples.

API documentation must include usage examples and error scenarios.