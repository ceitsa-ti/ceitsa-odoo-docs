# Local Development Setup Guide

This guide will help you set up a local development environment for Odoo 17 Enterprise.

## Prerequisites

### System Requirements
- Ubuntu 20.04/22.04 LTS (recommended) or Windows 10/11 with WSL2
- Python 3.8+
- PostgreSQL 13+
- Node.js 14+ (for frontend assets)
- Git

### Required Packages (Ubuntu)
```bash
sudo apt update
sudo apt install -y git python3-pip python3-dev python3-venv \
    python3-wheel libxml2-dev libpq-dev libjpeg8-dev \
    liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev \
    libldap2-dev build-essential git libssl-dev libffi-dev \
    libmariadb-dev libmariadb-dev-compat libmariadb3 \
    libmariadbclient-dev libmariadb-dev-compat libmariadb-dev \
    libssl-dev libsasl2-dev libldap2-dev libjpeg-dev \
    libjpeg8-dev libjpeg-turbo8-dev libjpeg-turbo8 \
    libopenjp2-7-dev liblcms2-dev libwebp-dev \
    tcl8.6-dev tk8.6-dev libxml2-dev libxslt-dev \
    zlib1g-dev libfreetype6-dev libffi-dev libpq-dev \
    libjpeg8-dev liblcms2-dev libopenblas-dev \
    libatlas-base-dev libblas-dev liblapack-dev \
    libx11-6 libxext6 libxrender1 libxss1 libxtst6 \
    libnss3-dev libgconf-2-4 libfontconfig1 libxkbcommon0 \
    libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
    libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 \
    libxcb-xinput0 libxcb-xkb1 xvfb
```

## Setup Steps

### 1. Clone the Repository
```bash
git clone https://github.com/ceitsa-ti/ceitsa-odoo-docs.git
cd ceitsa-odoo-docs
```

### 2. Set Up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Odoo and Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL
```bash
# Create PostgreSQL user
sudo -u postgres createuser -s $USER
createdb $USER

# Create Odoo database user
sudo -u postgres createuser odoo
createdb odoo
```

### 5. Configure Odoo
Create a configuration file at `~/.odoorc` or in your project directory as `odoo.conf`:

```ini
[options]
; Basic Configuration
addons_path = /path/to/your/addons
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo
db_password = False
http_port = 8069

; Development Options
dev = all
log_level = debug
```

### 6. Initialize the Database
```bash
createdb -O odoo my_odoo_db
```

### 7. Start Odoo
```bash
python3 odoo-bin -c odoo.conf
```

## Common Issues

### Port Already in Use
```bash
# Find and kill the process using the port
sudo lsof -i :8069
kill -9 <PID>

# Or change the port in odoo.conf
http_port = 8070
```

### Database Connection Issues
- Ensure PostgreSQL is running: `sudo service postgresql status`
- Check user permissions: `psql -U odoo -d postgres -c "\du"`
- Verify database exists: `psql -U odoo -l`

## Development Tools

### Recommended VS Code Extensions
- Python
- Pylance
- XML Tools
- Odoo Snippets
- GitLens
- Docker
- ESLint
- Prettier

### Debugging
1. Install debugpy:
   ```bash
   pip install debugpy
   ```

2. Add to your Odoo command:
   ```bash
   python3 -m debugpy --listen 0.0.0.0:3001 odoo-bin -c odoo.conf
   ```

3. Configure VS Code launch.json:
   ```json
   {
       "name": "Python: Remote Attach",
       "type": "python",
       "request": "attach",
       "connect": {
           "host": "localhost",
           "port": 3001
       },
       "pathMappings": [
           {
               "localRoot": "${workspaceFolder}",
               "remoteRoot": "."
           }
       ]
   }
   ```

## Best Practices

### Git Workflow
1. Always create a new branch for features/fixes:
   ```bash
   git checkout -b 17.0-feature/feature-name
   ```

2. Commit often with meaningful messages:
   ```bash
   git commit -m "[ADD] module_name: add new feature"
   ```

3. Keep your branch updated:
   ```bash
   git fetch origin
   git rebase origin/17.0
   ```

### Code Style
- Follow [Odoo's coding guidelines](https://www.odoo.com/documentation/17.0/developer/reference/guidelines.html)
- Use pre-commit hooks for code quality
- Write docstrings for all methods and classes

## Next Steps

1. Set up your IDE for Odoo development
2. Configure your database backup strategy
3. Set up a staging environment
4. Implement CI/CD pipelines

## Support
For assistance, contact the CEITSA IT Department.
