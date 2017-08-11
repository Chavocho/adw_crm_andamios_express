# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

  ae_metodo_pago = fields.Selection( [('efectivo','Efectivo'),('cheque', 'Cheque'),('transferencia', 'Transferencia'),('tarjeta_de_debito', 'Tarjeta de Débito'),('tarjeta_de_credito', 'Tarjeta de Crédito'),('deposito_efectivo', 'Deposito en Efectivo'),('otros', 'Otros')], 'Método de Pago', help="Método de Pago")
  ae_servicio = fields.Selection( [('andamiaje_y_accesorios','Andamiaje y Accesorios'),('puntal_y_cimbra', 'Puntal y Cimbra'),('servicios', 'Servicios')], 'Servicio Solicitado', help="Servicio Solicitado")
  ae_tipo_cotizacion = fields.Selection([('venta','Venta'),('renta', 'Renta')], 'Tipo de Cotización', help="Tipo de Cotización")
