# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api
from datetime import date,timedelta

class stockTransport(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle', string="vehicle", help="Many2one with vehicle. display the details of vehicle model in fleet")
    vehicle_catagory_id = fields.Many2one('fleet.vehicle.model.category', string="Vehicle Catagory")
    per_volume = fields.Float(compute="_compute_volume", store=True, help="total volume calculated for progressbar")
    per_weight = fields.Float(compute="_compute_weight", store=True, help="total weight calculated for progressbar")
    date_start = fields.Date('Date start', required=True, index=True, default=date.today())
    date_finished = fields.Date('Date To', required=True, index=True, default=date.today() + timedelta(days=2))
    total_weight = fields.Float(compute="_total_weight")
    total_volume = fields.Float(compute="_total_volume")

    @api.depends('picking_ids', 'picking_ids.move_line_ids.product_id.weight','vehicle_catagory_id')
    def _compute_weight(self):
        for record in self:
            weight = record.vehicle_catagory_id.max_weight
            if weight:
                record.per_weight = (sum(picking.weight for picking in record.picking_ids) / weight) * 100

    @api.depends('picking_ids', 'picking_ids.move_line_ids.product_id.volume', 'vehicle_catagory_id')
    def _compute_volume(self):
        for record in self:
            volume = record.vehicle_catagory_id.max_volume
            if volume:
                record.per_volume = ( sum(picking.volume for picking in record.picking_ids) / volume) * 100

    @api.depends('per_weight', 'per_volume', 'name')
    def _compute_display_name(self):
        for record in self:
            if record.vehicle_catagory_id:
                record.display_name = f"{record.name} ({record.total_weight} kg, {record.total_volume} m³):{record.vehicle_id.driver_id.name or ''}"
            else:
                record.display_name = f"{record.name}"

    @api.depends('per_weight')
    def _total_weight(self):
        for record in self:
            record.total_weight = round(sum(picking.weight for picking in record.picking_ids),2)

    @api.depends('per_volume')
    def _total_volume(self):
        for record in self:
            record.total_volume = round(sum(picking.volume for picking in record.picking_ids),2)
