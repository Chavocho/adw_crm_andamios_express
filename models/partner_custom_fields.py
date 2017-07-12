# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PartnerCustomFields(models.Model):
  _inherit = "res.partner"

  ae_domicilio_obra     = fields.Char(string="Domicilio de Obra", help="Domicilio de Obra")
  ae_razon_social       = fields.Char(string="Razón Social", help="Razón Social")
  ae_domicilio_fiscal   = fields.Char(string="Domicilio Fiscal", help="Domicilio Fiscal")
  ae_rfc                = fields.Char( string="RFC", help="RFC")
  ae_contrato_nuevo     = fields.Boolean( string="Contrato Nuevo", help="Contrato Nuevo")
