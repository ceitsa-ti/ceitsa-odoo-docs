# CEITSA Odoo Development Documentation

Welcome to the official documentation repository for CEITSA's Odoo development workflow, standards, and best practices.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Workflow](#development-workflow)
3. [Module Development](#module-development)
4. [Deployment Process](#deployment-process)
5. [Best Practices](#best-practices)
6. [Troubleshooting](#troubleshooting)

## Getting Started

### Prerequisites
- Odoo SH access
- GitHub account with repository access
- Local development environment

### Local Setup
```bash
git clone https://github.com/ceitsa-ti/ceitsa-odoo-docs.git
cd ceitsa-odoo-docs
```

## Development Workflow

Our workflow follows these main stages:
1. **Development** → **Testing** → **Staging** → **Production**

### Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation updates

## Module Development

### Creating a New Module
1. Use the module template from `templates/MODULE_TEMPLATE.md`
2. Follow Odoo's module structure
3. Document your module in the README

## Deployment Process

### Staging Deployment
1. Merge feature branches into `develop`
2. Test in staging environment
3. Create pull request to `main`

### Production Deployment
1. Merge `develop` into `main`
2. Tag the release
3. Deploy to production

## Best Practices

### Code Style
- Follow PEP 8
- Use meaningful variable names
- Document complex logic

### Git Commit Messages
- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Include details in the body if needed

## Troubleshooting

### Common Issues
1. **Module not found**
   - Check `__manifest__.py` for dependencies
   - Verify module is in the addons path

2. **Database connection issues**
   - Verify database credentials
   - Check if the database exists and is accessible

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Abraham Vega - Lead Developer
- CEITSA IT Department
