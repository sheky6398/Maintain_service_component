from odoo import models,fields
import logging

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"




    product_ids = fields.Many2many('service.material',string="Product")