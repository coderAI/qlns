# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class DanhMuc(models.Model):
    _name = 'danh.muc'

    code = fields.Integer(string='Mã Danh Mục')
    name = fields.Char(string='Tên Danh Mục', required=True)
    type = fields.Selection([('in','Thu'),('out','Chi')],string = u'Loại Danh Mục')

