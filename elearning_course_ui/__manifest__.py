# __manifest__.py
{
    "name": "E-learning Course UI",
    "summary": "Enhances eLearning course pages with pricing info and custom request access flow.",
    "version": "1.0",
    "category": "eLearning",
    "author": "Ahmed Abed",
    "license": "LGPL-3",
    "depends": [
        "website_slides",
        "elearning_sales"
    ],
    "data": [
        "templates/course_price_box.xml",
        "templates/request_access_button.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_course_ui/static/src/scss/course.css',
        ],
    },

    "installable": True,
    "application": False,
}
