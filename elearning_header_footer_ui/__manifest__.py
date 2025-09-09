# __manifest__.py
{
    "name": "E-learning Header & Footer UI",
    "summary": "Customizes the navbar and removes Odoo footer watermark on eLearning pages.",
    "version": "1.0",
    "category": "eLearning",
    "author": "Ahmed Abed",
    "license": "LGPL-3",
    "depends": [
        "website",
        "website_slides"
    ],
    "data": [
        "templates/remove_footer_watermark.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_header_footer_ui/static/src/scss/navbar.css',
        ],
    },

    "installable": True,
    "application": False,
}
