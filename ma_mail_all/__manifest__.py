{
    "name": "Show all messages",
    "summary": """Checkout all messages where you have access""",
    "category": "Discuss",
    # "live_test_url": "",
    "images": ['images/1.jpg'],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    'price': 13.33,
    'currency': 'EUR',

    "depends": [
        "mail"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    'installable': True,
    "auto_install": False,
}
