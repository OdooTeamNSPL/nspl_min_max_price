from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    min_price = fields.Float(string="Minimum Price")
    max_price = fields.Float(string="Maximum Price")
