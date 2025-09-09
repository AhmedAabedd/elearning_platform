from odoo import models , fields, api, _



class GrantAccessWizard(models.TransientModel):
    _name = 'grant.access.wizard'


    activity_id = fields.Many2one('mail.activity')
    channel_id = fields.Many2one('slide.channel')
    partner_id = fields.Many2one('res.partner')
    sale_problem = fields.Selection([
        ('no_confirm', 'Not Confirm'),
        ('no', 'No Sale'),
    ])

    def action_confirm_grant_access(self):
        self.ensure_one()
        self.channel_id.action_grant_access(self.partner_id.id)
    
    def action_create_sale_order(self):
        self.ensure_one()
        return self.activity_id.action_create_sale_order()