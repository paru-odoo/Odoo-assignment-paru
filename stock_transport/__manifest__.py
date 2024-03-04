# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Stock Transport',
    'version':'1.0',
    'depends': ['base', 'stock_picking_batch', 'fleet', 'stock_delivery', 'delivery'],
    'data':[
        'security/ir.model.access.csv',

        'views/st_catagory.xml',
        'views/st_batch_transfer_trans.xml',
        'views/st_batch_transfering.xml'
    ],
    'author': "Odoo",
    'category':'Stock Transport/Brokerage',
    'sequence':'1',
    'installable': True,
    'auto_install': True,    
    'license': 'LGPL-3'
}
