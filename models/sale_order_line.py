# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class SaleOrderLine(models.Model):
  _inherit = "sale.order"

  ae_dias_renta     = fields.Char(string="Dias de renta", help="")
