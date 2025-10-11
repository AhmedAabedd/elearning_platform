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
        'views/courses.xml',
        'views/jobs.xml',
        'views/job_position.xml',
        'views/contact_us.xml',
        #'views/sign_in.xml',
        'views/connection_security.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_website_pages_ui/static/src/css/home.css',
            'elearning_website_pages_ui/static/src/css/courses.css',
            'elearning_website_pages_ui/static/src/css/signin.css',
            'elearning_website_pages_ui/static/src/css/contact_us.css',
            'elearning_website_pages_ui/static/src/css/jobs.css',
            'elearning_website_pages_ui/static/src/css/connection_security.css',
        ],
    },

    "installable": True,
    "application": False,
}
