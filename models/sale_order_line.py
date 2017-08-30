# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = amount_days_retail = rent_amount_untaxed = 0.0
            if order.ae_tipo_cotizacion == 'cotizacion_para_renta':
                if order.ae_renta_dia <= 0:
                    order.ae_renta_dia = 1
                for line in order.order_line:
                    if line.product_id.type == 'service':
                        amount_untaxed += line.price_subtotal
                        amount_tax += line.price_tax
                    else:
                        amount_untaxed += (line.price_subtotal * order.ae_renta_dia)
                        amount_tax += (line.price_tax * order.ae_renta_dia)

                    rent_amount_untaxed += line.price_subtotal
                    amount_days_retail = order.ae_renta_dia
            else:
                for line in order.order_line:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                    rent_amount_untaxed = 0
                    amount_days_retail = 1
            order.update({
                'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
                'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
                'rent_amount_untaxed': order.pricelist_id.currency_id.round(rent_amount_untaxed),
                'amount_days_retail':  order.pricelist_id.currency_id.round(amount_days_retail),
                'amount_total': (amount_untaxed + amount_tax),
            })

    ae_tipo_cotizacion = fields.Selection([('cotizacion_para_venta', 'Cotización para Venta'), ('cotizacion_para_renta', 'Cotización para Renta')], string='Tipo de Cotización',
                                     readonly=True,states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                     default='cotizacion_para_venta')
    ae_renta_dia = fields.Integer(string='Días de Renta', default=1, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})

    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all',
                                     track_visibility='always')
    rent_amount_untaxed = fields.Monetary(string='Untaxed Amount Rent', store=True, readonly=True, compute='_amount_all',
                                     track_visibility='always')
    amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_all',
                                 track_visibility='always')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all',
                                   track_visibility='always')
    amount_days_retail = fields.Integer(string='Días de Renta', store=True, readonly=True, compute='_amount_all',
                                   track_visibility='always')

    @api.onchange('ae_tipo_cotizacion', 'ae_renta_dia', 'order_line')
    def supply_rate(self):
        for order in self:
            order.amount_untaxed = order.amount_tax = order.amount_total = order.rent_amount_untaxed = 0.0
            if order.ae_tipo_cotizacion == 'cotizacion_para_renta':
                if order.ae_renta_dia <= 0:
                    order.ae_renta_dia = 1
                for line in order.order_line:
                    if line.product_id.type == 'service':
                        order.amount_untaxed += line.price_subtotal
                        order.amount_tax += line.price_tax
                    else:
                        order.amount_untaxed += (line.price_subtotal * order.ae_renta_dia)
                        order.amount_tax += (line.price_tax * order.ae_renta_dia)

                    order.rent_amount_untaxed += line.price_subtotal
                    order.amount_days_retail = order.ae_renta_dia
            else:
                for line in order.order_line:
                    order.amount_untaxed += line.price_subtotal
                    order.amount_tax += line.price_tax
                    order.rent_amount_untaxed = 0
                    order.amount_days_retail = 1
            order.amount_total = order.amount_untaxed + order.amount_tax

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    ae_dias_renta_line = fields.Integer(string='Días', default=3)
