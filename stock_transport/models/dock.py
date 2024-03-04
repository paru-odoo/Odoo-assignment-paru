# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api

class stockTransportcatagory(models.Model):
    _name = 'dock'
    
    name = fields.Char(string = "Dock")
