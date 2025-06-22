---
name: Copilot Autonomous Development Task
about: Create a task for GitHub Copilot autonomous implementation
title: "[Copilot Task] "
labels: ["copilot-task", "autonomous-development"]
assignees: []
---

## Problem Description
<!-- Clear, specific description of what needs to be implemented and why -->


## Context from PRD
**Reference Document**: {{PRD_DOCUMENT_PATH}}
**Technical Specification**: {{TECHNICAL_SPEC_PATH}}
**Architecture Layer**: <!-- {{ARCHITECTURE_LAYERS_OPTIONS}} -->

## Acceptance Criteria
<!-- Specific, testable requirements with checkboxes -->
- [ ] 
- [ ] 
- [ ] 
- [ ] Performance target: <!-- {{PERFORMANCE_TARGET_EXAMPLE}} -->
- [ ] Test coverage: >{{TEST_COVERAGE_THRESHOLD}}%
- [ ] Architecture compliance validated
- [ ] Documentation updated with examples

## Files to Create/Modify
<!-- Explicit list of files that need to be created or modified -->
- `{{EXAMPLE_SOURCE_PATH}}/` - 
- `{{EXAMPLE_TEST_PATH}}/` - 
- `{{EXAMPLE_BENCH_PATH}}/` - 

## Architecture Requirements
**{{ARCHITECTURE_PATTERN}} Compliance**:
- [ ] Follow dependency rules (inner layers don't depend on outer layers)
- [ ] Implement in correct layer as specified above
- [ ] Use dependency inversion with {{INTERFACE_PATTERN}}
- [ ] Pass simple data structures across boundaries

**{{PRIMARY_LANGUAGE}} Conventions** (from `.github/copilot-instructions.md`):
{{#each LANGUAGE_CONVENTIONS}}
- [ ] {{this}}
{{/each}}

## Performance Requirements
<!-- Specific benchmarks from copilot-context.md -->
- **Target**: <!-- {{PERFORMANCE_TARGET_EXAMPLE}} -->
- **Memory**: <!-- {{MEMORY_TARGET_EXAMPLE}} -->
- **Benchmark Command**: `{{BENCHMARK_COMMAND_EXAMPLE}}`

## Dependencies
<!-- List any modules or features this task depends on -->
- [ ] <!-- dependency 1 -->
- [ ] <!-- dependency 2 -->

## Definition of Done
- [ ] All acceptance criteria completed
- [ ] Performance benchmarks met or exceeded
- [ ] Test coverage >{{TEST_COVERAGE_THRESHOLD}}% with meaningful assertions
- [ ] {{ARCHITECTURE_PATTERN}} compliance validated
- [ ] Documentation includes usage examples and error scenarios
- [ ] Integration tests pass
- [ ] Code follows conventions from `.github/copilot-instructions.md`

## Quality Validation
**Before marking as complete, run**:
```bash
# Build and test
{{BUILD_COMMAND}}
{{TEST_COMMAND}}
{{BENCHMARK_COMMAND}}

# Coverage check
{{COVERAGE_COMMAND}}

# Architecture validation
{{ARCHITECTURE_VALIDATION_COMMAND}}

# Format and lint
{{FORMAT_COMMAND}}
{{LINT_COMMAND}}
```

## References
- **Copilot Instructions**: `.github/copilot-instructions.md`
- **Project Context**: `.github/copilot-context.md`
- **Setup Steps**: `.github/copilot-setup-steps.yml`
- **Configuration**: `project-config.yml`

---
**Note for Copilot**: This issue is designed for autonomous implementation. All necessary context is provided in the referenced files. Follow the {{ARCHITECTURE_PATTERN}} principles and performance requirements strictly.