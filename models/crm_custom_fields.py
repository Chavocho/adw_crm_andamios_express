# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

  # ae_servicio           = fields.Selection(string="Servicio", help="Servicio solicitado", required=True, selection=[(30, 30), (45, 45), (60, 60)])
