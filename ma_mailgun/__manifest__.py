{
    "name": """Mailgun""",
    "summary": """Setup the outgoing and incoming mail flow easily by using Mailgun""",
    "category": "Discuss",
    "images": ["images/mailgun_main.png"],
    "version": "12.0.1.1.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 129.00,
    "currency": "EUR",

    "depends": [
        "mail",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'data/ir_cron_data.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Mailgun",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "mailgun",
    "demo_summary": "Easy to send outgoing and fetch incoming messages by using Mailgun",
    "demo_images": [
        "images/mailgun_main.png",
    ]
}
