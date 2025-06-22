# {{PROJECT_NAME}} - Project Context

## Project Overview
**Mission**: {{PROJECT_MISSION}}
**Description**: {{PROJECT_DESCRIPTION}}

## Domain Knowledge
{{PROJECT_DOMAIN_CONTEXT}}

## Target Users
{{#each TARGET_USERS}}
- **{{ROLE}}**: {{DESCRIPTION}}
{{/each}}

## Core Value Proposition
{{#each VALUE_PROPOSITIONS}}
- {{this}}
{{/each}}

## Technical Architecture
**Architecture Pattern**: {{ARCHITECTURE_PATTERN}}
**Technology Stack**: 
- Backend: {{BACKEND_LANGUAGE}}/{{BACKEND_FRAMEWORK}}
- Frontend: {{FRONTEND_LANGUAGE}}/{{FRONTEND_FRAMEWORK}}
{{#if DATABASE_TYPE}}
- Database: {{DATABASE_TYPE}}
{{/if}}
{{#if DEPLOYMENT_PLATFORM}}
- Deployment: {{DEPLOYMENT_PLATFORM}}
{{/if}}

## Key Technical Decisions
{{#each TECHNICAL_DECISIONS}}
### {{DECISION}}
**Rationale**: {{RATIONALE}}
**Implications**: {{IMPLICATIONS}}
{{/each}}

## Performance Requirements
{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: {{TARGET}} ({{CONTEXT}})
{{/each}}

## Integration Requirements
{{#each INTEGRATIONS}}
- **{{NAME}}**: {{PURPOSE}} ({{API_DETAILS}})
{{/each}}

## Development Timeline
**Total Duration**: {{TIMELINE_DAYS}} days
**Key Milestones**:
{{#each TIMELINE_PHASES}}
- **Days {{DAYS}}**: {{NAME}} - {{DESCRIPTION}}
{{/each}}

## Reference Documents
- **PRD**: {{PRD_REFERENCE}}
{{#if TECHNICAL_SPEC_REFERENCE}}
- **Technical Specification**: {{TECHNICAL_SPEC_REFERENCE}}
{{/if}}
{{#if API_REFERENCE}}
- **API Reference**: {{API_REFERENCE}}
{{/if}}
{{#if DESIGN_DOCS}}
- **Design Documents**: {{DESIGN_DOCS}}
{{/if}}

## Success Metrics
{{#each SUCCESS_METRICS}}
- **{{CATEGORY}}**: {{METRICS}}
{{/each}}

## Constraints and Assumptions
{{#each CONSTRAINTS}}
- {{this}}
{{/each}}

## Clean Architecture Layer Definitions

### Entities (Innermost Layer)
Domain models and business rules that are independent of external concerns:
{{#each ENTITY_EXAMPLES}}
- **{{NAME}}**: {{DESCRIPTION}}
{{/each}}

### Use Cases (Application Business Rules)
Application-specific business rules that orchestrate the flow of data to and from entities:
{{#each USE_CASE_EXAMPLES}}
- **{{NAME}}**: {{DESCRIPTION}}
{{/each}}

### Interface Adapters
Convert data between use cases/entities and external agencies:
{{#each ADAPTER_EXAMPLES}}
- **{{NAME}}**: {{DESCRIPTION}}
{{/each}}

### Frameworks & Drivers (Outermost Layer)
External agencies like databases, web frameworks, UI:
{{#each FRAMEWORK_EXAMPLES}}
- **{{NAME}}**: {{DESCRIPTION}}
{{/each}}

## Dependency Rules
- Source code dependencies can only point inwards
- Inner layers know nothing about outer layers
- Data that crosses boundaries is simple data structures
- We don't pass Entity objects or Database rows across boundaries