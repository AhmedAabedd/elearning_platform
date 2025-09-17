from odoo import models, fields, api




class SlideChannel(models.Model):
    _inherit = 'slide.channel'



    is_featured = fields.Boolean(string="Show in Featured", default=False)