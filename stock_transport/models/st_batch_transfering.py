# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from odoo.exceptions import ValidationError

class stockTransportcatagory(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle', string="vehicle", help="Many2one with vehicle. display the details of vehicle model in fleet")
    vehicle_catagory_id = fields.Many2one('fleet.vehicle.model.category', string="Vehicle Catagory")
    max_volume = fields.Float(compute="_compute_volume")
    max_weight = fields.Float(compute="_compute_weight")

    def _compute_weight(self):
        for record in self:
            total_weight = 0.0
            max_weight = record.vehicle_catagory_id.max_weight
            if max_weight == 0:
                raise ValidationError("max weight must be greater than 0.") 
            for picking in record.picking_ids:
                total_weight += picking.shipping_weight
            record.max_weight = (total_weight / max_weight) * 100

    def _compute_volume(self):
        for record in self:
            total_volume = 0.0
            max_volume = record.vehicle_catagory_id.max_volume
            if max_volume == 0:
                raise ValidationError("max volume / product of value : must be greater than 0.") 
            for picking in record.picking_ids:
                total_volume += picking.volume
            record.max_volume = (total_volume / max_volume) * 100
