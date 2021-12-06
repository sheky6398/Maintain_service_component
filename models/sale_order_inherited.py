from odoo import models,api
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.model_create_multi
    def create(self, vals_list):
        """ This Method will override create Method of sale order and when we select the product it is checking what's the product type if product type is service and, it has a components than it will create a delivery order for service type product that has a components.
        """
        # result = super(SaleOrder,self).create(vals_list)
        # _logger.info(f'\nRESULT+++++{result}\n')
        
        # for rec in result:
        #     for sale_order_line in rec.order_line:
        #         if sale_order_line.product_id.type == 'service' and sale_order_line.product_id.product_ids:
        #             _logger.info(f'\n SERVICE PRODUCT AND COMPONENTS\n')
        #             #Create a new sale order line for service type product
        #             for components in sale_order_line.product_id.product_ids:
        #                 new_order_line = self.env['sale.order.line']
        #                 new_order_line.create({
        #                     'product_id': components.product_id.id,
        #                     'product_uom_qty' : components.quantity,
        #                     'order_id' : result.id,
        #                     'name':  components.product_id.name
        #                 })
        
        # return result
        
        for record in vals_list:
                _logger.info(f'\n SERVICE PRODUCT AND COMPONENTS={vals_list}\n')
                for sale_order_line in record.get('order_line'):

                    if sale_order_line.product_id :
                        pass

 
            

        result = super(SaleOrder,self).create(vals_list)
        return result          
