# -*- coding: utf-8 -*-
{
    'name': 'E-learning Access Requests',
    'version': '1.0.0',
    'category': 'eLearning',
    'summary': 'Manage course access requests from the course form view',
    'description': """
                        eLearning Access Requests
                        =========================

                        This module extends Odoo eLearning to make access requests easier to manage:

                        - Adds a smart button on the course (slide.channel) form view.
                        - Displays the number of pending requests.
                        - Allows internal users to view, accept, or refuse requests directly from the course, 
                        instead of managing them only through the chatter.
                            """,
    'author': 'Ahmed Abed',
    'license': 'LGPL-3',
    'depends': [
        'website_slides',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/grant_access_wizard_view.xml',
        'views/inherit_slide_channel_view.xml',
        'views/mail_activity_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
