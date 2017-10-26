# -*- coding: utf-8 -*-
{
    'name': 'Valida precio unitario en presupuestos y pedidos',
    'version': '1.1',
    'category': 'SO',
    'description': """
    No podrá guardar y/o confirmar cotizaciones/pedidos si el precio unitario es cambiado a un precio menor al que calcula la tarifa.
    """,
    'author': 'Humanytek',
    'website': 'http://www.humanytek.com',
    'depends': ['sale'],
    'data': [
        #'sale_order.xml',
        'security/groups.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
