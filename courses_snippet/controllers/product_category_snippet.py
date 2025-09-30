from odoo import http
from odoo.http import request




class WebsiteProduct(http.Controller):


    
    @http.route('/get_featured_courses', auth="public", type='json', website=True)
    def get_product_category(self):

        """ public_categs = request.env['product.public.category'].sudo().search_read(
            [('parent_id', '=', False)], fields=['name', 'image_1920', 'id']
        ) """

        featured_courses = request.env['slide.channel'].sudo().search_read(
            [('is_featured', '=', True)], fields=['name', 'image_1920', 'id', 'featured_description', 'total_time']
        )

        values = {
            'courses': featured_courses,
        }
        return values