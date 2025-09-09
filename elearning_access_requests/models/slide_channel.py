from odoo import models, fields, api



class SlideChannel(models.Model):
    _inherit = 'slide.channel'


    request_count = fields.Integer(compute="_compute_request_count")
    
    def _compute_request_count(self):
        for rec in self:
            rec.request_count = self.env['mail.activity'].search_count([
                ('res_model', '=', 'slide.channel'),
                ('res_id', '=', rec.id),
                ('activity_type_id', '=', self.env.ref('website_slides.mail_activity_data_access_request').id)
            ])
    
    def action_view_access_requests(self):
        self.ensure_one()
        activity_type_id = self.env.ref('website_slides.mail_activity_data_access_request').id
        
        return {
            'type': 'ir.actions.act_window',
            'name': f'Access Requests - {self.name}',
            'res_model': 'mail.activity',
            'view_mode': 'list,form',
            'views': [(self.env.ref('elearning_access_requests.view_course_access_activities_tree').id, 'list'), (False, 'form')],
            'domain': [
                ('res_model', '=', 'slide.channel'),
                ('res_id', '=', self.id),
                ('activity_type_id', '=', activity_type_id)
            ],
            'context': {
                'default_res_model': 'slide.channel',
                'default_res_id': self.id,
                'default_activity_type_id': activity_type_id,
            },
            'target': 'current',
        }
    
    