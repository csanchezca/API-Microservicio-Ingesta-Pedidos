# odoo_module_design/models.py
"""
Este archivo corresponde a un diseño de módulo Odoo.
No está destinado a ejecutarse fuera del entorno Odoo.
"""
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_order_number = fields.Integer(string="Order Number", required=True)

    x_external_company = fields.Selection(
        selection=[
            ("ecommerce", "ecommerce"),
            ("manual", "manual"),
            ("Amazon", "Amazon"),
        ],
        string="External Company",
    )

    x_is_big_order = fields.Boolean(
        string="Is Big Order",
        compute="_compute_x_is_big_order",
        store=True,
    )

    @api.depends("amount_total")
    def _compute_x_is_big_order(self):
        for order in self:
            order.x_is_big_order = order.amount_total > 500

    @api.constrains("x_order_number")
    def _check_x_order_number_min(self):
        for order in self:
            # Permite vacío/0 si aún no se asigna (opcional). Si quieres forzar obligatorio, lo cambiamos.
            if order.x_order_number and order.x_order_number < 10:
                raise ValidationError("El campo x_order_number debe ser mayor o igual que 10.")
