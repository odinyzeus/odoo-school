# -*- coding: utf-8 -*-
{
    'name': "Scholar Managment Module",

    'summary': "Lets to de manager get control about asistant and administratives process of the alumns",

    'description': """
        With this module the mananager of publics school could control all admnistratives process
    """,

    'author': "Dr. T.A. Eduardo Vargas Bernardino",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academics',
    'installable': True,
    'auto_install': False,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

