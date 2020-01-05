{
    "name": """Internal Messaging""",
    "summary": """Send private messages to specified recipients, regardless of who are in followers list.""",
    "category": "Discuss",
    "images": ['images/mail_private_image.png'],
    "version": "12.0.1.1.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 16.66,
    "currency": "EUR",

    "depends": [
        "mail"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'template.xml',
        'full_composer_wizard.xml',
    ],
    "demo": [
    ],
    "qweb": [
        'static/src/xml/mail_private.xml',
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
