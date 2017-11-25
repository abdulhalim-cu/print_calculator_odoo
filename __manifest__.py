# -*- coding: utf-8 -*-
{
    'name': "Calculator",
    'summary': """Simple Calculator""",
    'description': """
        Simple calculator:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
    """,
    'author': "Abdul Halim",
    'website': "https://abdulhalim.pythonanywhere.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'calculator/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}