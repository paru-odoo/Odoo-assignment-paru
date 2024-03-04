# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api

class st_batch_transfer_trans(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", readonly=True, compute = '_cal_volume')

    @api.depends('move_ids')
    def _cal_volume(self):
        for record in self:
            volumes = map(lambda move: move.product_id.volume * move.quantity, record.move_ids)
            record.volume = sum(volumes)
