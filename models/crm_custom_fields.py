# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

 # ae_servicio           = fields.Selection(string="Servicio", help="Servicio solicitado", required=True, selection=[('andamiaje_y_accesorios','Andamiaje y Accesorios'),('puntal_y_cimbra', 'Puntal y Cimbra'),('servicios', 'Servicios')])
