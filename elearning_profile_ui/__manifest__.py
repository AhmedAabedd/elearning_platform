# __manifest__.py
{
    "name": "E-learning Profile UI",
    "summary": "Customizes website profile pages: header, menu, badges, XP, and branding.",
    "version": "1.0",
    "category": "eLearning",
    "author": "Ahmed Abed",
    "license": "LGPL-3",
    "depends": ["website_profile"],
    "data": [
        "templates/dropdown_list_account_button.xml",
        "templates/profile_page.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'elearning_profile_ui/static/src/scss/hide_card_xp.css',
        ],
    },
    "installable": True,
    "application": False,
}
