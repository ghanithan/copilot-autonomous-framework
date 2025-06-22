# Integration Review Command

## Purpose
Analyze code changes for integration patterns, API design, and external service interactions.

## Usage
`@claude /review-integration`

## Review Criteria

### 1. API Design & Standards
- [ ] **RESTful Design**: Proper HTTP methods and status codes
- [ ] **API Versioning**: Version management strategy
- [ ] **Request/Response**: Consistent data formats
- [ ] **Documentation**: API endpoints documented

### 2. Error Handling & Resilience
- [ ] **Error Propagation**: Proper error handling chain
- [ ] **Retry Logic**: Appropriate retry strategies
- [ ] **Circuit Breakers**: Failure isolation mechanisms
- [ ] **Timeout Handling**: Request timeout management

### 3. Data Consistency & Transactions
- [ ] **ACID Properties**: Transaction boundaries defined
- [ ] **Data Integrity**: Consistency constraints enforced
- [ ] **Distributed Transactions**: Multi-service coordination
- [ ] **Eventual Consistency**: Async operation handling

### 4. Communication Patterns
- [ ] **Synchronous**: Request-response patterns
- [ ] **Asynchronous**: Event-driven communication
- [ ] **Message Queues**: Reliable message delivery
- [ ] **Event Sourcing**: Event-based state management

### 5. Authentication & Authorization
- [ ] **Service Authentication**: Inter-service auth
- [ ] **API Security**: Endpoint protection
- [ ] **Token Management**: JWT/OAuth implementation
- [ ] **Rate Limiting**: API usage controls

## Review Output Format

```markdown
## Integration Review Results

### 🔗 Integration Strengths
- Well-designed API interfaces
- Robust error handling and resilience
- Proper authentication and security

### ⚠️ Integration Concerns
- API design inconsistencies with file:line references
- Missing error handling scenarios
- Integration reliability issues

### 🚨 Critical Integration Issues
- Security vulnerabilities in API endpoints
- Data consistency problems
- Service communication failures

### 🔧 Integration Recommendations
1. API design improvements with examples
2. Error handling and resilience enhancements
3. Performance and reliability optimizations

### 🌐 Integration Score: X/10
Based on API design, reliability, and security assessment.
```

## External Service Integration Patterns

### HTTP Client Best Practices
- [ ] **Connection Pooling**: Efficient connection reuse
- [ ] **Request Timeouts**: Appropriate timeout values
- [ ] **Response Validation**: Status code and content validation
- [ ] **Error Classification**: Transient vs permanent errors

### Database Integration
- [ ] **Connection Management**: Pool configuration and lifecycle
- [ ] **Query Optimization**: Efficient database queries
- [ ] **Transaction Management**: Proper transaction boundaries
- [ ] **Migration Strategy**: Database schema evolution

### Message Queue Integration
- [ ] **Message Durability**: Persistent message delivery
- [ ] **Dead Letter Queues**: Failed message handling
- [ ] **Message Ordering**: Sequence preservation when needed
- [ ] **Consumer Scaling**: Horizontal scaling patterns

### Cache Integration
- [ ] **Cache Strategy**: Appropriate caching patterns
- [ ] **Cache Invalidation**: Consistent cache updates
- [ ] **Cache Warming**: Proactive cache population
- [ ] **Cache Fallback**: Graceful cache failure handling

## API Design Validation

### RESTful API Patterns
- [ ] **Resource Modeling**: Clear resource hierarchy
- [ ] **HTTP Methods**: Appropriate verb usage (GET, POST, PUT, DELETE)
- [ ] **Status Codes**: Meaningful HTTP status responses
- [ ] **Content Negotiation**: Support for multiple formats

### GraphQL Patterns (if applicable)
- [ ] **Schema Design**: Well-structured GraphQL schema
- [ ] **Query Complexity**: Query depth and complexity limits
- [ ] **Resolver Efficiency**: N+1 query prevention
- [ ] **Error Handling**: GraphQL error response patterns

### gRPC Patterns (if applicable)
- [ ] **Service Definition**: Clear protocol buffer definitions
- [ ] **Streaming**: Appropriate use of streaming RPCs
- [ ] **Error Codes**: Proper gRPC error handling
- [ ] **Load Balancing**: Client-side load balancing

## Integration Resilience Patterns

### Circuit Breaker Pattern
- [ ] **Failure Detection**: Automatic failure detection
- [ ] **State Management**: Open/closed/half-open states
- [ ] **Recovery Logic**: Automatic recovery attempts
- [ ] **Monitoring**: Circuit breaker state monitoring

### Retry Strategies
- [ ] **Exponential Backoff**: Progressive retry delays
- [ ] **Jitter**: Randomization to prevent thundering herd
- [ ] **Max Attempts**: Bounded retry attempts
- [ ] **Idempotency**: Safe retry operations

### Bulkhead Pattern
- [ ] **Resource Isolation**: Separate resource pools
- [ ] **Failure Containment**: Isolated failure domains
- [ ] **Thread Pools**: Dedicated execution contexts
- [ ] **Connection Pools**: Isolated connection resources

## Data Integration Patterns

### Event-Driven Architecture
- [ ] **Event Schema**: Well-defined event structures
- [ ] **Event Versioning**: Backward compatibility
- [ ] **Event Ordering**: Sequence preservation
- [ ] **Event Replay**: Historical event processing

### Saga Pattern (for distributed transactions)
- [ ] **Choreography**: Event-based coordination
- [ ] **Orchestration**: Central coordinator pattern
- [ ] **Compensation**: Rollback transaction logic
- [ ] **State Management**: Saga state tracking

### CQRS Pattern (if applicable)
- [ ] **Command Side**: Write operation optimization
- [ ] **Query Side**: Read operation optimization
- [ ] **Event Store**: Event sourcing implementation
- [ ] **Projection Updates**: View materialization

## Security Integration

### API Security
- [ ] **Authentication**: Identity verification mechanisms
- [ ] **Authorization**: Role-based access control
- [ ] **Rate Limiting**: API usage throttling
- [ ] **Input Validation**: Request data sanitization

### Service-to-Service Communication
- [ ] **Mutual TLS**: Encrypted service communication
- [ ] **Service Mesh**: Traffic encryption and routing
- [ ] **API Gateways**: Centralized security enforcement
- [ ] **Secret Management**: Secure credential handling

## Performance Integration

### Latency Optimization
- [ ] **Connection Reuse**: HTTP keep-alive and pooling
- [ ] **Compression**: Request/response compression
- [ ] **Caching**: Strategic caching implementation
- [ ] **CDN Usage**: Content delivery optimization

### Scalability Patterns
- [ ] **Load Balancing**: Traffic distribution strategies
- [ ] **Auto Scaling**: Dynamic resource allocation
- [ ] **Database Sharding**: Horizontal data partitioning
- [ ] **Read Replicas**: Read operation scaling

## Integration Testing Strategy

### Contract Testing
- [ ] **Consumer Contracts**: Client expectation validation
- [ ] **Provider Contracts**: Service capability validation
- [ ] **Contract Evolution**: Breaking change detection
- [ ] **Mock Services**: Test environment simulation

### End-to-End Testing
- [ ] **User Journeys**: Complete workflow validation
- [ ] **Data Flow**: Information flow across services
- [ ] **Error Scenarios**: Failure mode testing
- [ ] **Performance Testing**: Integration performance validation

## Common Integration Anti-Patterns

### Design Issues
- Chatty interfaces with excessive round trips
- Overly complex API designs
- Inconsistent error handling across services
- Missing API versioning strategy

### Reliability Issues
- Missing retry logic for transient failures
- Inadequate timeout configuration
- Poor error classification and handling
- Missing circuit breaker implementation

### Security Issues
- Unencrypted service-to-service communication
- Missing authentication for internal APIs
- Inadequate input validation
- Exposed sensitive data in API responses

### Performance Issues
- Synchronous calls where async would be better
- Missing connection pooling
- Inefficient data serialization
- Lack of caching for expensive operations

## Context Integration
This command uses project-specific integration requirements from CLAUDE.md:

### External Integrations
{{#each INTEGRATIONS}}
- **{{name}}**: {{purpose}}
  - API Details: {{api_details}}
  - Review Focus: Authentication, error handling, data flow
{{/each}}

### Technology Stack Integration Points
- Backend framework integration patterns
- Database and persistence layer integration
- Frontend-backend communication
- Third-party service integration

Reviews ensure robust, secure, and performant integration implementations that support the overall system architecture.