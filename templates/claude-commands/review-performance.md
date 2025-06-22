# Performance Review Command

## Purpose
Analyze code changes for performance characteristics, optimization opportunities, and benchmark compliance.

## Usage
`@claude /review-performance`

## Review Criteria

### 1. Algorithm Efficiency
- [ ] **Time Complexity**: Analyze Big O notation for algorithms
- [ ] **Space Complexity**: Evaluate memory usage patterns
- [ ] **Data Structures**: Appropriate choice for use case
- [ ] **Algorithm Selection**: Optimal algorithms for problem domain

### 2. Resource Management
- [ ] **Memory Usage**: Efficient allocation and deallocation
- [ ] **CPU Utilization**: Minimize unnecessary computations
- [ ] **I/O Operations**: Optimize file and network operations
- [ ] **Resource Cleanup**: Proper disposal of resources

### 3. Concurrency & Async Patterns
- [ ] **Thread Safety**: Safe concurrent access patterns
- [ ] **Async/Await**: Proper async operation handling
- [ ] **Deadlock Prevention**: Avoid blocking dependencies
- [ ] **Resource Contention**: Minimize lock contention

### 4. Database Performance
- [ ] **Query Optimization**: Efficient database queries
- [ ] **Indexing Strategy**: Proper index usage
- [ ] **N+1 Problem**: Avoid excessive database calls
- [ ] **Connection Pooling**: Efficient connection management

### 5. Caching Strategy
- [ ] **Cache Usage**: Appropriate caching mechanisms
- [ ] **Cache Invalidation**: Proper cache lifecycle
- [ ] **Memory Caching**: In-memory optimization
- [ ] **Distributed Caching**: Multi-instance considerations

## Review Output Format

```markdown
## Performance Review Results

### ⚡ Performance Highlights
- Well-optimized areas meeting performance targets
- Efficient algorithms and data structures used

### 🐌 Performance Concerns
- Specific bottlenecks with file:line references
- Algorithm complexity issues
- Resource management problems

### 📊 Benchmark Compliance
{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: Target {{TARGET}} - [PASS/FAIL/UNKNOWN]
{{/each}}

### 🔧 Optimization Recommendations
1. Specific performance improvements with examples
2. Algorithm or data structure alternatives
3. Caching and optimization strategies

### 📈 Performance Score: X/10
Based on efficiency, scalability, and benchmark compliance.
```

## Technology-Specific Checks

### Rust Performance Patterns
- [ ] **Zero-Cost Abstractions**: Leverage Rust's efficiency
- [ ] **Memory Safety**: No unnecessary heap allocations
- [ ] **Iterator Chains**: Use efficient iterator patterns
- [ ] **Async Runtime**: Proper tokio usage patterns

### Python Performance Patterns
- [ ] **List Comprehensions**: Use where appropriate
- [ ] **Generator Functions**: Memory-efficient iteration
- [ ] **NumPy/Pandas**: Vectorized operations for data processing
- [ ] **Async Operations**: Proper asyncio usage

### Frontend Performance Patterns
- [ ] **Bundle Size**: Minimize JavaScript bundle size
- [ ] **Lazy Loading**: Component and route lazy loading
- [ ] **Memoization**: React.memo and useMemo usage
- [ ] **Virtual Scrolling**: Large list optimization

## Common Performance Anti-Patterns

### Algorithm Issues
- Nested loops where single loop possible
- Inefficient sorting algorithms
- Linear search where hash lookup available
- Recursive solutions without memoization

### Resource Issues
- Memory leaks from unclosed resources
- Excessive object creation in loops
- Blocking I/O in async contexts
- Thread pool exhaustion

### Database Issues
- N+1 query problems
- Missing database indexes
- Inefficient JOIN operations
- Large data transfers without pagination

### Caching Issues
- Cache stampede problems
- Inappropriate cache TTL values
- Missing cache warming strategies
- Cache invalidation race conditions

## Performance Testing Recommendations

### Benchmarking
- Unit-level performance tests
- Integration performance validation
- Load testing scenarios
- Stress testing limits

### Monitoring
- Performance metric collection
- Real-time performance alerts
- Resource usage tracking
- Response time monitoring

## Context Integration
This command uses project-specific performance targets from CLAUDE.md:
{{#each PERFORMANCE_TARGETS}}
- **{{METRIC}}**: {{TARGET}} ({{CONTEXT}})
{{/each}}

Reviews are tailored to the technology stack and domain requirements specified in the project context.