# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class NguonThu(models.Model):
    _name = 'nguon.thu'

    name = fields.Char(string='Tên', required=True)
    description = fields.Text(string='Tên', required=True)
    opportunity_id = fields.Many2one(
        'danh.muc', u'Loại', domain="[('type', '=', 'in')]")
    total = fields.Integer(string= 'Số Tiền')
    date = fields.Date(string='Ngày Thu' )
