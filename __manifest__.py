# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'ADW Campos Adicionales CRM Andamios Express',
    'author': 'ADWEB Solutions',
    'category': 'Tools',
    'summary': 'Campos adicionales Clientes, Oportunidades',
    'website': 'http://www.adwebsolutions.com',
    'depends': ['crm','sale', 'report'],
    'data': [
        'views/partner_custom_fields.xml',
        'views/crm_custom_fields.xml',
        'views/sale_order_line.xml',
        'views/sale_order_report.xml',
        'views/theme.xml',
    ],
    'installable': True,
}
