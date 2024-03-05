# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from dateutil.relativedelta import relativedelta

class stockTransport(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle', string="vehicle", help="Many2one with vehicle. display the details of vehicle model in fleet")
    vehicle_catagory_id = fields.Many2one('fleet.vehicle.model.category', string="Vehicle Catagory")
    max_volume = fields.Float(compute="_compute_volume", store=True, help="total volume calculated for progressbar")
    max_weight = fields.Float(compute="_compute_weight", store=True, help="total weight calculated for progressbar")
    date_start = fields.Date('Date start', required=True, index=True,default=fields.Date.today())
    date_finished = fields.Date('Date To', required=True, index=True, default=fields.Date.today() + relativedelta(days=2))

    @api.depends('vehicle_catagory_id', 'picking_ids', 'move_line_ids.product_id.weight')
    def _compute_weight(self):
        for record in self:
            max_weight = record.vehicle_catagory_id.max_weight
            if max_weight:
                record.max_weight = (sum(picking.weight for picking in record.picking_ids) / max_weight) * 100

    @api.depends('move_line_ids.product_id.volume', 'vehicle_catagory_id', 'picking_ids')
    def _compute_volume(self):
        for record in self:
            max_volume = record.vehicle_catagory_id.max_volume
            if max_volume:
                record.max_volume = (sum(picking.volume for picking in record.picking_ids) / max_volume) * 100

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for category in self:
            if category.vehicle_catagory_id:
                category.display_name = f"{category.name} ({category.max_weight} kg, {category.max_volume} m3): {category.vehicle_id.driver_id.name}"
            else:
                category.display_name = f"{category.name}"
