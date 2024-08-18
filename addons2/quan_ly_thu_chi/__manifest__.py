# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'quan ly thu chi',
    'version' : '1.2',   
    'sequence': 10,
    'description': """
quan ly thu chi""",
    'depends': [],
    'data': [
        'security/quan_ly_thu_chi_security.xml',
        'security/ir.model.access.csv',        
        'views/qltc_views.xml',      
        'views/qltc_menu_views.xml',
    ],

    'license': 'LGPL-3',
}
