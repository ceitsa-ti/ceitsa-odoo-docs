#!/usr/bin/env python3
"""
PDF Generator for CEITSA Odoo Documentation

This script converts the Markdown documentation to a professional PDF.

Prerequisites:
    pip install markdown weasyprint
"""

import os
import markdown
from datetime import datetime
from weasyprint import HTML, CSS

def generate_pdf():
    """Generate a PDF from the Markdown documentation."""
    # File paths
    md_file = 'CEITSA_ODOO_DEVELOPMENT_GUIDE.md'
    output_pdf = 'CEITSA_ODOO_DEVELOPMENT_GUIDE.pdf'
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Add last updated timestamp
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    footer = f"\n\n---\n*Document generated on: {last_updated}*"
    footer += "\n*For the latest version, visit: https://github.com/ceitsa-ti/ceitsa-odoo-docs*"
    
    if not md_content.endswith(footer):
        md_content += footer
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['tables'])
    
    # Create a complete HTML document with styling
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>CEITSA Odoo Development Guide</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-right {{
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 10pt;
                }}
                @bottom-left {{
                    content: "CEITSA Odoo Development Guide";
                    font-size: 10pt;
                }}
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
                margin: 0 auto;
                padding: 0;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #2c3e50;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
            }}
            h1 {{
                color: #1a5276;
                border-bottom: 2px solid #1a5276;
                padding-bottom: 0.3em;
            }}
            h2 {{
                border-bottom: 1px solid #eee;
                padding-bottom: 0.3em;
            }}
            code {{
                background-color: #f5f5f5;
                padding: 0.2em 0.4em;
                border-radius: 3px;
                font-family: 'Courier New', Courier, monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f8f9fa;
                border: 1px solid #eaecf0;
                border-radius: 3px;
                padding: 1em;
                overflow: auto;
            }}
            a {{
                color: #1a5276;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .header-logo {{
                text-align: center;
                margin-bottom: 2em;
            }}
            .header-logo img {{
                max-width: 200px;
                height: auto;
            }}
            .footer {{
                margin-top: 2em;
                font-size: 0.8em;
                color: #666;
                text-align: center;
                border-top: 1px solid #eee;
                padding-top: 1em;
            }}
        </style>
    </head>
    <body>
        <div class="header-logo">
            <!-- Add your logo here if needed -->
            <h1>CEITSA Odoo Development Guide</h1>
        </div>
        
        <div class="content">
            {content}
        </div>
        
        <div class="footer">
            <p>© {year} CEITSA. All rights reserved.</p>
            <p>For the latest version, visit: https://github.com/ceitsa-ti/ceitsa-odoo-docs</p>
        </div>
    </body>
    </html>
    """.format(
        content=html_content,
        year=datetime.now().year
    )
    
    # Generate PDF
    HTML(string=html_doc).write_pdf(
        output_pdf,
        stylesheets=[
            CSS(string='')
        ]
    )
    
    print(f"PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    generate_pdf()
