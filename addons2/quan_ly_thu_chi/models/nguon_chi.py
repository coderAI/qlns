# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class NguonChi(models.Model):
    _name = 'nguon.chi'

    name = fields.Char(string='Tên', required=True)
    description = fields.Text(string='Ghi Chú', required=True)
    opportunity_id = fields.Many2one(
        'danh.muc', string= 'Loại', domain="[('type', '=', 'out')]")
    total = fields.Integer(string= 'Số Tiền')
    date = fields.Date(string='Ngày Chi' )
