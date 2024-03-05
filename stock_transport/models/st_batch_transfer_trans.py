# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api

class st_batch_transfer_trans(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute = '_cal_volume')
    weight = fields.Float(string="Weight", compute = '_cal_weight')

    @api.depends('move_ids')
    def _cal_volume(self):
        for picking in self:
            picking.volume = sum(move.product_id.volume * move.quantity for move in picking.move_ids)

    @api.depends('move_ids')
    def _cal_weight(self):
        for picking in self:
            picking.weight = sum(move.product_id.weight * move.quantity for move in picking.move_ids)
