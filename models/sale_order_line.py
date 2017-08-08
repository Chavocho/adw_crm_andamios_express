# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    ae_dias_renta_line = fields.Integer(string='Días', default=1)
