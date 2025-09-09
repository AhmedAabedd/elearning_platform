from odoo import api, models, fields, _
from odoo.exceptions import UserError



class MailActivity(models.Model):
    _inherit = 'mail.activity'


    #partner_sale_done = fields.Boolean(compute="_compute_partner_sale_done", default=True)
    partner_sale_done = fields.Selection([
        ('no', 'No Sale'),
        ('no_confirm', 'Not Confirm'),
        ('yes', 'Yes'),
    ], compute="_compute_partner_sale_done")

    def _compute_partner_sale_done(self):
        for activity in self:
            activity.partner_sale_done = 'no'
            if activity.res_model == 'slide.channel' and activity.res_id and activity.request_partner_id:
                channel = self.env['slide.channel'].browse(activity.res_id)
                
                sale_order = self.env['sale.order'].search([
                    ('partner_id', '=', activity.request_partner_id.id)
                ]).filtered(lambda so: channel.product_template_id in so.order_line.mapped('product_template_id'))

                if sale_order:
                    activity.partner_sale_done = 'no_confirm'
                    if sale_order.state in ['sale', 'done']:
                        activity.partner_sale_done = 'yes'

    def action_create_sale_order(self):
        self.ensure_one()
        if self.res_model == 'slide.channel' and self.res_id and self.request_partner_id:
            channel = self.env['slide.channel'].browse(self.res_id)

            return {
                'type': 'ir.actions.act_window',
                'name': 'Create Sale Order',
                'res_model': 'sale.order',
                'view_mode': 'form',
                'target': 'new',   # opens in modal
                'context': {
                    'default_partner_id': self.request_partner_id.id,
                    'default_order_line': [(0, 0, {
                        'product_template_id': channel.product_template_id.id,
                        'product_id': channel.product_template_id.product_variant_id.id,
                        'product_uom_qty': 1,
                    })],
                },
            }
            

    def action_grant_course_access(self):
        """Grant access from activity"""
        for activity in self:
            if activity.res_model == 'slide.channel' and activity.res_id and activity.request_partner_id:
                # Store values BEFORE calling methods that might delete the activity
                channel_id = activity.res_id
                partner_id = activity.request_partner_id.id
                
                channel = self.env['slide.channel'].browse(channel_id)
                
                activity._compute_partner_sale_done()

                if activity.partner_sale_done in ['no', 'no_confirm']:
                    return {
                        'type': 'ir.actions.act_window',
                        'name': 'Grant Access Warning',
                        'res_model': 'grant.access.wizard',
                        'view_mode': 'form',
                        'target': 'new',   # opens in modal
                        'context': {
                            'default_activity_id': activity.id,
                            'default_channel_id': channel.id,
                            'default_partner_id': partner_id,
                            'default_sale_problem': activity.partner_sale_done,
                        },
                    }

                channel.action_grant_access(partner_id)

    def action_refuse_course_access(self):
        """Refuse access from activity"""
        for activity in self:
            if activity.res_model == 'slide.channel' and activity.res_id and activity.request_partner_id:
                # Store values BEFORE calling methods that might delete the activity
                channel_id = activity.res_id
                partner_id = activity.request_partner_id.id
                partner_name = activity.request_partner_id.name
                
                channel = self.env['slide.channel'].browse(channel_id)
                channel.action_refuse_access(partner_id)