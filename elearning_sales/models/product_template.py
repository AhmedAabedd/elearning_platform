from odoo import models, fields, api




class ProductTemplate(models.Model):
    _inherit = 'product.template'



    is_course_access = fields.Boolean(string="Course Access", default=False)