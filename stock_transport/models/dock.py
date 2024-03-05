# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api

class Dock(models.Model):
    _name = 'dock'

    name = fields.Char(string = "Dock", help="Name of dock")

    _sql_constraints = [("name", "UNIQUE(name)", "Name should not be repeated")]
