# -*- coding: utf-8 -*-
{
    'name': 'Courses snippet',
    'version': '1.0.0',
    'category': 'eLearning',
    'summary': '',
    'description': """
                    eLearning Courses Snippet
                    ===============

                    """,
    'author': 'Ahmed Abed',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_sale'
    ],
    'data': [
        'views/inherit_slide_channel_view.xml',
        'views/snippets/category_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/courses_snippet/static/src/xml/category_highlight_content.xml',
            '/courses_snippet/static/src/js/product_category.js',
        ],
    },

    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
