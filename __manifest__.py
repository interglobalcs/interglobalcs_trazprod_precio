# -*- coding: utf-8 -*-
{
    'name': "Módulo para agregar publicar producto y agrega trazabilidad",

    'summary': """
        Módulo para agregar publicar producto y agrega trazabilidad""",

    'description': """
        Módulo para agregar publicar producto y agrega trazabilidad
    """,

    'author': "InterGlobalCS",
    'website': "http://www.interglobalcs.com",

    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
