from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_violation = fields.Boolean(string="Price Violation", compute="_compute_price_violation", store=True)
    # price_violation = fields.Boolean(string="Price Violation", compute="_compute_price_violation", store=True)
    currency_id = fields.Many2one(related='order_id.currency_id', store=True, readonly=True)

    min_price = fields.Float(
        string="Min Price", compute="_compute_min_max_price", store=True
    )
    max_price = fields.Float(
        string="Max Price", compute="_compute_min_max_price", store=True
    )

    @api.depends('product_id')
    def _compute_min_max_price(self):
        for line in self:
            line.min_price = line.product_id.min_price or 0.0
            line.max_price = line.product_id.max_price or 0.0


    @api.depends('price_unit', 'min_price', 'max_price')
    def _compute_price_violation(self):
        for line in self:
            if line.min_price and line.price_unit < line.min_price:
                line.price_violation = True
            elif line.max_price and line.price_unit > line.max_price:
                line.price_violation = True
            else:
                line.price_violation = False

    @api.onchange('price_unit', 'product_id')
    def _onchange_price_unit(self):
        for line in self:
            if not line.product_id:
                continue
            min_price = line.product_id.min_price
            max_price = line.product_id.max_price

            if min_price and line.price_unit < min_price:
                return {
                    'warning': {
                        'title': "Minimum Price Warning",
                        'message': f"The price {line.price_unit} is below the minimum ({min_price})"
                    }
                }
            if max_price and line.price_unit > max_price:
                return {
                    'warning': {
                        'title': "Maximum Price Warning",
                        'message': f"The price {line.price_unit} exceeds the maximum ({max_price})"
                    }
                }

    @api.constrains('price_unit', 'product_id', 'order_id')
    def _check_min_max_price(self):
        for line in self:
            product = line.product_id
            user = self.env.user
            if product:
                min_price = product.min_price
                max_price = product.max_price

                if ((min_price and line.price_unit < min_price) or
                    (max_price and line.price_unit > max_price)):
                    if not user.has_group('nspl_min_max_price.group_allow_confirm_order'):
                        raise ValidationError(
                            f"Price of '{product.name}' must be between {min_price or 'N/A'} and {max_price or 'N/A'}."
                        )
