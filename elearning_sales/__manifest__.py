# -*- coding: utf-8 -*-
{
    'name': 'E-learning Sales',
    'version': '1.0.0',
    'category': 'eLearning',
    'summary': 'Link courses with products and manage related sales',
    'description': """
                    eLearning Sales
                    ===============

                    This module extends Odoo eLearning by integrating with Sales:

                    - Adds a link between courses (slide.channel) and products via a Many2one field.
                    - Displays the sales price of the course, taken from the linked product.
                    - Adds a smart button on the course form view showing the total revenue 
                    from confirmed sales of that course.
                    - Allows internal users to manage all sales orders related to the course directly.
                        """,
    'author': 'Ahmed Abed',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_slides'
    ],
    'data': [
        'views/inherit_product_view.xml',
        'views/inherit_slide_channel_view.xml',
        'views/slide_channel_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
