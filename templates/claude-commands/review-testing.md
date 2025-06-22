# Testing Review Command

## Purpose
Evaluate test coverage, quality, and testing strategy for code changes.

## Usage
`@claude /review-testing`

## Review Criteria

### 1. Test Coverage Analysis
- [ ] **Coverage Percentage**: Meets minimum {{TEST_COVERAGE_THRESHOLD}}% threshold
- [ ] **Branch Coverage**: All code paths tested
- [ ] **Function Coverage**: All functions have tests
- [ ] **Line Coverage**: Critical lines covered

### 2. Test Quality Assessment
- [ ] **Test Isolation**: Tests are independent and repeatable
- [ ] **Assertion Quality**: Clear and specific assertions
- [ ] **Test Data**: Appropriate test data and fixtures
- [ ] **Edge Cases**: Boundary conditions tested

### 3. Test Structure & Organization
- [ ] **Test Naming**: Clear, descriptive test names
- [ ] **Test Organization**: Logical grouping and structure
- [ ] **Setup/Teardown**: Proper test lifecycle management
- [ ] **Test Documentation**: Clear test intent and expectations

### 4. Testing Strategy Validation
- [ ] **Unit Tests**: Core business logic covered
- [ ] **Integration Tests**: Component interactions tested
- [ ] **Contract Tests**: API contracts validated
- [ ] **Performance Tests**: Critical paths benchmarked

### 5. Mock & Stub Usage
- [ ] **Appropriate Mocking**: External dependencies mocked
- [ ] **Mock Verification**: Mock interactions verified
- [ ] **Test Doubles**: Proper use of stubs, fakes, spies
- [ ] **Dependency Injection**: Testable design patterns

## Review Output Format

```markdown
## Testing Review Results

### ✅ Testing Strengths
- Well-covered areas with comprehensive tests
- Good testing practices implemented

### ⚠️ Testing Gaps
- Missing test coverage with file:line references
- Weak or incomplete test scenarios
- Testing anti-patterns identified

### 📊 Coverage Analysis
- **Overall Coverage**: X% (Target: {{TEST_COVERAGE_THRESHOLD}}%)
- **Branch Coverage**: X%
- **Function Coverage**: X%
- **Critical Path Coverage**: X%

### 🧪 Test Quality Issues
1. Specific test improvements needed
2. Missing edge cases and boundary tests
3. Flaky or unreliable tests

### 📋 Testing Recommendations
1. Additional test scenarios to implement
2. Testing strategy improvements
3. Test refactoring suggestions

### 🎯 Testing Score: X/10
Based on coverage, quality, and strategy completeness.
```

## Technology-Specific Testing Patterns

### Rust Testing
- [ ] **Unit Tests**: Inline tests in modules
- [ ] **Integration Tests**: Tests directory structure
- [ ] **Doc Tests**: Example code in documentation
- [ ] **Benchmark Tests**: Performance testing with criterion

### Python Testing
- [ ] **pytest Framework**: Modern testing practices
- [ ] **Test Fixtures**: Reusable test setup
- [ ] **Parametrized Tests**: Data-driven testing
- [ ] **Mock Library**: Proper mocking usage

### Frontend Testing
- [ ] **Component Tests**: React/Vue component testing
- [ ] **User Interaction**: Event handling tests
- [ ] **Snapshot Tests**: UI regression prevention
- [ ] **E2E Tests**: Full user journey testing

## Test Types & Strategies

### Unit Testing
- **Purpose**: Test individual functions/classes in isolation
- **Scope**: Single unit of code
- **Dependencies**: Mocked external dependencies
- **Speed**: Fast execution (< 1ms per test)

### Integration Testing
- **Purpose**: Test component interactions
- **Scope**: Multiple units working together
- **Dependencies**: Real or test implementations
- **Speed**: Moderate execution (< 100ms per test)

### Contract Testing
- **Purpose**: API contract validation
- **Scope**: Service boundaries
- **Dependencies**: Consumer/provider contracts
- **Speed**: Fast to moderate execution

### Performance Testing
- **Purpose**: Validate performance requirements
- **Scope**: Critical performance paths
- **Dependencies**: Realistic test environment
- **Speed**: Varies by benchmark complexity

## Common Testing Anti-Patterns

### Test Quality Issues
- Tests that test implementation details
- Overly complex test setup
- Tests with multiple assertions testing different things
- Flaky tests with timing dependencies

### Coverage Issues
- Gaming coverage metrics without testing behavior
- Missing edge case and error condition tests
- Inadequate boundary value testing
- Ignoring critical path coverage

### Test Organization Problems
- Poorly named tests that don't describe intent
- Monolithic test methods testing multiple scenarios
- Inconsistent test structure across codebase
- Missing or inadequate test documentation

### Mock/Stub Issues
- Over-mocking leading to brittle tests
- Testing mocks instead of behavior
- Inconsistent mock setup across tests
- Missing mock verification

## Performance Testing Validation

### Benchmark Requirements
{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: {{TARGET}} ({{CONTEXT}})
  - [ ] Performance test exists
  - [ ] Benchmark meets target
  - [ ] Regression testing in place
{{/each}}

### Load Testing
- [ ] **Concurrent Users**: Multi-user scenarios
- [ ] **Data Volume**: Large dataset handling
- [ ] **Resource Limits**: Memory/CPU constraints
- [ ] **Failure Scenarios**: Graceful degradation

## Testing Automation

### CI/CD Integration
- [ ] **Automated Execution**: Tests run on every commit
- [ ] **Fast Feedback**: Quick test suite for rapid iteration
- [ ] **Coverage Reporting**: Coverage trends tracked
- [ ] **Quality Gates**: Minimum coverage enforced

### Test Environment
- [ ] **Environment Parity**: Test environment matches production
- [ ] **Data Management**: Test data lifecycle management
- [ ] **Cleanup Procedures**: Proper test cleanup
- [ ] **Parallel Execution**: Tests can run concurrently

## Architecture Testing

### Clean Architecture Validation
- [ ] **Dependency Tests**: Verify dependency rules
- [ ] **Layer Isolation**: Test layer boundaries
- [ ] **Interface Contracts**: Validate abstractions
- [ ] **Business Rule Tests**: Core logic validation

### Design Pattern Testing
- [ ] **Pattern Implementation**: Correct pattern usage
- [ ] **Pattern Benefits**: Expected behavior achieved
- [ ] **Pattern Constraints**: Limitations respected
- [ ] **Pattern Evolution**: Changes don't break pattern

## Context Integration
This command leverages project-specific testing requirements:
- Minimum coverage thresholds from CLAUDE.md
- Technology stack testing frameworks
- Performance testing requirements
- Domain-specific testing scenarios

Testing reviews ensure code quality and maintainability while supporting the autonomous development workflow.