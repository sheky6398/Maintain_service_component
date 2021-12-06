from odoo import models,fields
import logging

_logger = logging.getLogger(__name__)


class ServiceType(models.Model):
    _name = "service.material"
    _description = "Product Type"
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product',string="Products", domain="[('type','=', 'product')]")
    quantity = fields.Float(string="Quantity")



