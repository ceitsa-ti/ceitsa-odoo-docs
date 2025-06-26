# CEITSA Odoo Development Guide

## Overview
This document provides a concise guide to CEITSA's Odoo development workflow and standards. For the most up-to-date version, please visit our [GitHub repository](https://github.com/ceitsa-ti/ceitsa-odoo-docs).

## Quick Start

### Repository Structure
```
ceitsa-odoo-docs/
├── README.md          # Main documentation
├── guides/            # Detailed guides
├── templates/         # Code templates
└── workflows/         # GitHub workflows
```

### Development Workflow
1. **Branch Naming**
   - `17.0-feature/feature-name` - New features
   - `17.0-fix/bug-description` - Bug fixes
   - `17.0-docs/update-docs` - Documentation updates

2. **Development Process**
   - Create a new branch from `17.0`
   - Make your changes
   - Commit with clear messages
   - Push to remote
   - Create a Pull Request

## Module Development

### Quick Start
1. Use the module template from `templates/MODULE_TEMPLATE.md`
2. Follow Odoo's module structure
3. Document your module

### Best Practices
- Use `ceitsa_` prefix for module names
- Follow Odoo's coding guidelines
- Write tests for new functionality
- Document complex logic

## Deployment

### Staging
1. Push to feature branch
2. Test in Odoo SH
3. Move to staging for validation

### Production
1. Create PR to `17.0`
2. Get approval
3. Merge and deploy

## Resources

### Documentation
- [Odoo 17 Documentation](https://www.odoo.com/documentation/17.0/)
- [Odoo Development Cookbook](https://www.packtpub.com/product/odoo-15-development-cookbook-fifth-edition/9781803242789)

### Support
For assistance, contact:
- Abraham Vega (Lead Developer)
- CEITSA IT Department

---
*Document generated on: 2025-06-26*
*For the latest version, visit: https://github.com/ceitsa-ti/ceitsa-odoo-docs*
