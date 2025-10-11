from odoo import models, fields, api
from odoo.exceptions import UserError



class SaleOrder(models.Model):
    _inherit = 'sale.order'



    @api.model_create_multi
    def create(self, vals):
        record = super().create(vals)
        for order in self:
            for line in order.order_line:
                if line.product_template_id:
                    if line.product_template_id.is_course_access:
                        course = self.env['slide.channel'].search([('enroll', '=', 'invite'), ('product_template_id', '=', line.product_template_id.id)], limit=1)
                        course.recompute_sales_total()
                        course.recompute_sales_count()
        return record

    def write(self, vals):
        res = super().write(vals)
        if 'order_line' in vals or 'state' in vals:
            for order in self:
                for line in order.order_line:
                    if line.product_template_id:
                        if line.product_template_id.is_course_access:
                            course = self.env['slide.channel'].search([('enroll', '=', 'invite'), ('product_template_id', '=', line.product_template_id.id)], limit=1)
                            if course:
                                course.recompute_sales_total()
                                course.recompute_sales_count()
        return res
    
    def unlink(self):
        for order in self:
            for line in order.order_line:
                if line.product_template_id:
                    if line.product_template_id.is_course_access:
                        course = self.env['slide.channel'].search([('enroll', '=', 'invite'), ('product_template_id', '=', line.product_template_id.id)])
                        course.recompute_sales_total()
                        course.recompute_sales_count()
        res = super().unlink()
        return res





class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'



    @api.constrains('product_uom_qty')
    def check_product_uom_qty(self):
        for line in self:
            if line.product_template_id.type == 'service' and line.product_template_id.is_course_access:
                if line.product_uom_qty != 1:
                    raise UserError(
                        "Course access products must have a quantity of 1. "
                        f"Please set the quantity to 1 for '{line.product_template_id.name}'."
                    )
                
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Check if product_id is being set and if it's a course access product
            if vals.get('product_id'):
                product = self.env['product.product'].browse(vals['product_id'])
                if product.is_course_access:
                    course = self.env['slide.channel'].search([('product_template_id', '=', product.id)])
                    # Override the name with "Access to {product_name}"
                    vals['name'] = f"Access to: {course.name}"
        
        return super().create(vals_list)