# CEITSA Odoo Development Guide - PDF Generation

This document explains how to generate a PDF version of the CEITSA Odoo Development Guide.

## Prerequisites

### On Ubuntu/Debian:
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y build-essential python3-dev python3-pip python3-setuptools \
    python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

### On Windows:
1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Install GTK+ from [gtk.org](https://www.gtk.org/download/)

## Installation

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements-pdf.txt
   ```

## Generating the PDF

Run the following command to generate the PDF:

```bash
python generate_pdf.py
```

This will create a file named `CEITSA_ODOO_DEVELOPMENT_GUIDE.pdf` in the current directory.

## Customization

You can modify the following files to customize the PDF output:

1. `CEITSA_ODOO_DEVELOPMENT_GUIDE.md` - Edit the content of the guide
2. `generate_pdf.py` - Modify the styling and layout of the PDF

## Troubleshooting

### Missing Dependencies
If you encounter any missing dependencies, make sure all system packages are installed:

```bash
# On Ubuntu/Debian
sudo apt-get install -y build-essential python3-dev python3-pip python3-setuptools \
    python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# Then reinstall the Python packages
pip install -r requirements-pdf.txt --force-reinstall
```

### Font Issues
If you see font-related errors, install additional fonts:

```bash
# On Ubuntu/Debian
sudo apt-get install -y fonts-dejavu fonts-liberation
```

## License

This documentation is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
