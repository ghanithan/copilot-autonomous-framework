# Architecture Review Command

## Purpose
Review code changes for Clean Architecture compliance and design principle adherence.

## Usage
`@claude /review-architecture`

## Review Criteria

### 1. Clean Architecture Layer Separation
- [ ] **Entities**: Pure business objects with no external dependencies
- [ ] **Use Cases**: Application business rules, orchestrate entity interactions
- [ ] **Adapters**: Interface adapters (controllers, gateways, presenters)
- [ ] **Frameworks**: External concerns (web framework, database, UI)

### 2. Dependency Rule Compliance
- [ ] Dependencies point inward only (outer layers depend on inner layers)
- [ ] No inner layer references to outer layers
- [ ] Interfaces defined in inner layers, implemented in outer layers
- [ ] No framework dependencies in business logic

### 3. SOLID Principles Validation
- [ ] **Single Responsibility**: Each class/module has one reason to change
- [ ] **Open/Closed**: Open for extension, closed for modification
- [ ] **Liskov Substitution**: Subtypes are substitutable for base types
- [ ] **Interface Segregation**: Clients don't depend on unused methods
- [ ] **Dependency Inversion**: Depend on abstractions, not concretions

### 4. Design Pattern Assessment
- [ ] Appropriate use of design patterns
- [ ] No over-engineering or premature abstraction
- [ ] Clear separation of concerns
- [ ] Proper encapsulation and information hiding

## Review Output Format

```markdown
## Architecture Review Results

### ✅ Compliant Areas
- List areas that follow Clean Architecture principles correctly

### ⚠️ Areas for Improvement
- Specific violations with file:line references
- Suggested refactoring approaches
- Impact assessment of changes

### 🚨 Critical Issues
- Serious architecture violations
- Dependencies pointing outward
- Framework coupling in business logic

### 📋 Recommendations
1. Specific actionable improvements
2. Refactoring suggestions with examples
3. Additional patterns to consider

### 🎯 Architecture Score: X/10
Brief justification of score based on compliance levels.
```

## Common Issues to Flag

### Layer Violations
- Business logic in controllers
- Database queries in use cases
- UI components in entities
- Framework imports in business logic

### Dependency Issues
- Circular dependencies
- Tight coupling between modules
- Missing abstractions/interfaces
- Direct instantiation instead of injection

### Design Problems
- God classes with multiple responsibilities
- Anemic domain models
- Leaky abstractions
- Missing or inappropriate design patterns

## Context Integration
This command leverages the project context from CLAUDE.md including:
- Defined architecture layers and examples
- Technology stack constraints
- Domain-specific business rules
- Performance and quality requirements