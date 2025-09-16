# __manifest__.py
{
    "name": "E-learning Website Pages UI",
    "summary": "",
    "version": "1.0",
    "category": "eLearning",
    "author": "Ahmed Abed",
    "license": "LGPL-3",
    "depends": [
        "website",
        "website_slides",
    ],
    "data": [
        'views/home.xml',
        'views/home_templates.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_website_pages_ui/static/src/css/home.css',
            'elearning_website_pages_ui/static/src/css/courses.css',
        ],
    },

    "installable": True,
    "application": False,
}
