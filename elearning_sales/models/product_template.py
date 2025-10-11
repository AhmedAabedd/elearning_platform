from odoo import models, fields, api




class ProductTemplate(models.Model):
    _inherit = 'product.template'



    is_course_access = fields.Boolean(string="Course Access", default=False)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("is_course_access"):  #return none if is_course_access doesnt exist in the dict vals
                vals['name'] = f"(Course Access) {vals['name']}"
            
        rec = super().create(vals)
        return rec
    
    def write(self, vals):
        if vals.get('is_course_access'):
            for record in self:
                # Only update name if it's not already prefixed and we're not explicitly setting a new name
                if 'name' not in vals and not record.name.startswith("(Course Access) "):
                    vals['name'] = f"(Course Access) {record.name}"
    
        res = super().write(vals)
        return res