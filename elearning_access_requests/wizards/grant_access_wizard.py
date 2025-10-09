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
    order_id = fields.Many2one('sale.order', string="Sale Order", compute="_compute_order_id")

    @api.depends('sale_problem')
    def _compute_order_id(self):
        self.ensure_one()
        self.order_id = False
        if self.sale_problem == 'no_confirm':
            self.order_id = self.env['sale.order'].search([
                                ('partner_id', '=', self.activity_id.request_partner_id.id)
                            ], limit=1).filtered(lambda so: self.channel_id.product_template_id in so.order_line.mapped('product_template_id'))

    def action_confirm_grant_access(self):
        self.ensure_one()
        self.channel_id.action_grant_access(self.partner_id.id)
    
    def action_create_sale_order(self):
        self.ensure_one()
        return self.activity_id.action_create_sale_order()
    
    def action_confirm_order_grant_access(self):
        self.ensure_one()
        self._compute_order_id()
        self.order_id.state = 'sale'
        self.action_confirm_grant_access()