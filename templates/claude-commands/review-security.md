# Security Review Command

## Purpose
Analyze code changes for security vulnerabilities, best practices compliance, and threat mitigation.

## Usage
`@claude /review-security`

## Review Criteria

### 1. Input Validation & Sanitization
- [ ] **User Input**: All external input properly validated
- [ ] **SQL Injection**: Parameterized queries used
- [ ] **XSS Prevention**: Output encoding implemented
- [ ] **Path Traversal**: File path validation present

### 2. Authentication & Authorization
- [ ] **Authentication**: Proper user authentication mechanisms
- [ ] **Authorization**: Role-based access control implemented
- [ ] **Session Management**: Secure session handling
- [ ] **Token Security**: JWT/API token best practices

### 3. Data Protection
- [ ] **Encryption**: Sensitive data encrypted at rest/transit
- [ ] **Secrets Management**: No hardcoded credentials
- [ ] **PII Handling**: Personal data protection compliance
- [ ] **Data Masking**: Sensitive data properly masked in logs

### 4. Error Handling & Logging
- [ ] **Information Disclosure**: No sensitive data in errors
- [ ] **Error Messages**: Generic error responses to users
- [ ] **Logging Security**: Secure logging without sensitive data
- [ ] **Stack Traces**: No stack traces exposed to users

### 5. Cryptography
- [ ] **Algorithm Choice**: Strong cryptographic algorithms
- [ ] **Key Management**: Proper key generation and storage
- [ ] **Random Generation**: Cryptographically secure randomness
- [ ] **Hash Functions**: Appropriate hashing algorithms

## Review Output Format

```markdown
## Security Review Results

### 🔒 Security Strengths
- Well-implemented security controls
- Proper use of security best practices

### ⚠️ Security Concerns
- Potential vulnerabilities with file:line references
- Missing security controls
- Compliance gaps

### 🚨 Critical Security Issues
- High-risk vulnerabilities requiring immediate attention
- Data exposure risks
- Authentication/authorization bypasses

### 🛡️ Security Recommendations
1. Specific vulnerability fixes with examples
2. Additional security controls to implement
3. Compliance improvements needed

### 🔐 Security Score: X/10
Based on vulnerability assessment and security control coverage.
```

## Technology-Specific Security Checks

### Rust Security Patterns
- [ ] **Memory Safety**: Leverage Rust's built-in protections
- [ ] **Unsafe Blocks**: Justified and minimal unsafe usage
- [ ] **Integer Overflow**: Proper overflow handling
- [ ] **Serialization**: Safe deserialization practices

### Python Security Patterns
- [ ] **Pickle Safety**: Avoid unsafe pickle deserialization
- [ ] **eval() Usage**: No dynamic code execution
- [ ] **Path Injection**: Safe file path handling
- [ ] **Dependency Security**: Secure package usage

### Web Security Patterns
- [ ] **CORS Policy**: Proper cross-origin configuration
- [ ] **CSP Headers**: Content Security Policy implementation
- [ ] **HTTPS Enforcement**: TLS/SSL properly configured
- [ ] **Cookie Security**: Secure cookie attributes

## Common Security Vulnerabilities

### Injection Attacks
- SQL injection in database queries
- Command injection in system calls
- LDAP injection in directory queries
- NoSQL injection in document databases

### Authentication Issues
- Weak password policies
- Missing multi-factor authentication
- Session fixation vulnerabilities
- Insecure password storage

### Authorization Problems
- Missing access controls
- Privilege escalation vulnerabilities
- Insecure direct object references
- Function-level access control bypass

### Data Exposure
- Sensitive data in logs
- Information disclosure in error messages
- Unencrypted sensitive data storage
- Inadequate data transmission protection

### Cryptographic Issues
- Weak encryption algorithms
- Insecure key management
- Poor random number generation
- Improper certificate validation

## Security Testing Recommendations

### Static Analysis
- Code scanning for known vulnerabilities
- Dependency vulnerability scanning
- Secret detection in code
- Security linting rules

### Dynamic Testing
- Penetration testing scenarios
- Fuzzing for input validation
- Authentication/authorization testing
- Error handling validation

### Compliance Checks
- OWASP Top 10 coverage
- Industry-specific compliance (PCI DSS, HIPAA, GDPR)
- Security framework alignment
- Data protection requirements

## Integration Security

### API Security
- Rate limiting implementation
- API authentication mechanisms
- Input validation for all endpoints
- Response security headers

### Database Security
- Connection string protection
- Database access controls
- Encryption at rest
- Audit logging

### Third-Party Integrations
- Secure API communication
- Vendor security assessment
- Data sharing agreements
- Integration access controls

## Context Integration
This command considers project-specific security requirements from CLAUDE.md:
- Domain-specific compliance requirements
- Technology stack security patterns
- Integration security needs
- Performance vs security trade-offs

Security reviews are tailored to the specific threat model and compliance requirements of the project domain.