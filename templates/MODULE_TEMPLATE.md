# CEITSA Odoo Module Template

## Module Structure
```
ceitsa_<module_name>/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── controllers.py
├── models/
│   ├── __init__.py
│   └── models.py
├── security/
│   ├── ir.model.access.csv
│   └── <module_name>_security.xml
├── static/
│   ├── description/
│   │   └── icon.png
│   └── src/
│       ├── img/
│       ├── js/
│       └── scss/
├── views/
│   ├── templates.xml
│   ├── views.xml
│   └── <model>_views.xml
└── README.md
```

## __manifest__.py
```python
{
    'name': 'CEITSA Module Name',
    'version': '17.0.1.0.0',
    'category': 'CEITSA',
    'summary': 'Brief description of the module',
    'description': """
        Detailed description of the module's functionality
    """,
    'author': 'CEITSA',
    'website': 'https://www.ceitsa.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/<module_name>_security.xml',
        'views/<model>_views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
```

## Security Files

### ir.model.access.csv
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_<model>_user,<model>.user,model_<module>_<model>,base.group_user,1,1,1,0
access_<model>_manager,<model>.manager,model_<module>_<model>,base.group_system,1,1,1,1
```

### <module_name>_security.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record id="group_<module>_user" model="res.groups">
            <field name="name">User</field>
            <field name="category_id" ref="base.module_category_ceitsa"/>
        </record>
        
        <record id="group_<module>_manager" model="res.groups">
            <field name="name">Manager</field>
            <field name="category_id" ref="base.module_category_ceitsa"/>
            <field name="implied_ids" eval="[(4, ref('group_<module>_user'))]"/>
        </record>
    </data>
</odoo>
```

## Model Example
```python
from odoo import models, fields, api

class ExampleModel(models.Model):
    _name = 'ceitsa.example'
    _description = 'Example Model'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    date = fields.Date(string='Date', default=fields.Date.today)
    
    @api.model
    def create(self, vals):
        # Add custom create logic here
        return super(ExampleModel, self).create(vals)
    
    def write(self, vals):
        # Add custom write logic here
        return super(ExampleModel, self).write(vals)
```

## View Example
```xml
<odoo>
    <!-- Tree View -->
    <record id="view_example_tree" model="ir.ui.view">
        <field name="name">ceitsa.example.tree</field>
        <field name="model">ceitsa.example</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="date"/>
            </tree>
        </field>
    </record>
    
    <!-- Form View -->
    <record id="view_example_form" model="ir.ui.view">
        <field name="name">ceitsa.example.form</field>
        <field name="model">ceitsa.example</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="date"/>
                        </group>
                        <group>
                            <field name="active"/>
                        </group>
                    </group>
                    <notebook>
                        <page string="Description">
                            <field name="description"/>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>
    
    <!-- Action -->
    <record id="action_example" model="ir.actions.act_window">
        <field name="name">Examples</field>
        <field name="res_model">ceitsa.example</field>
        <field name="view_mode">tree,form</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first example!
            </p>
        </field>
    </record>
    
    <!-- Menu -->
    <menuitem id="menu_root" name="CEITSA"/>
    <menuitem id="menu_example_root" name="Examples" parent="menu_root"/>
    <menuitem id="menu_example" name="Examples" parent="menu_example_root" action="action_example"/>
</odoo>
```

## Best Practices

1. **Naming Conventions**
   - Module name: `ceitsa_<purpose>` (lowercase, underscores)
   - Model names: `ceitsa.<model_name>` (singular)
   - Field names: `lowercase_with_underscores`
   - View IDs: `view_<model>_<view_type>`
   - Security group IDs: `group_<module>_<group_name>`

2. **Security**
   - Always define proper access rights
   - Use security groups for access control
   - Never store sensitive data in the database without encryption

3. **Performance**
   - Use `@api.model` for class methods that don't need a recordset
   - Use `@api.multi` for methods that work with a recordset
   - Avoid heavy computations in `__init__` methods

4. **Testing**
   - Write tests for all major functionality
   - Test edge cases
   - Include demo data for testing

## Module README.md
```markdown
# CEITSA Module Name

## Description
Brief description of what the module does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation
1. Clone the repository
2. Add the module to your Odoo addons path
3. Install the module from the Apps menu

## Configuration
1. Go to Settings > Technical > System Parameters
2. Configure any required parameters

## Usage
Step-by-step instructions on how to use the module.

## Known Issues / Roadmap
- [ ] Known issue 1
- [ ] Planned feature 1

## Support
For support, contact the CEITSA IT Department.
```
