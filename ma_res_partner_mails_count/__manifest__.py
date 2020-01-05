{
    "name": """Partner mails count""",
    "summary": """Displays amount of incoming and outgoing partner mails.""",
    "category": "Discuss",
    "images": ['images/1.png'],
    "version": "1.0.0",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    "price": 10.00,
    "currency": "EUR",

    "depends": [
        'ma_mail_all',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/res_partner_mails_count.xml',
        'templates.xml',
    ],
    "demo": [
    ],
    "installable": False,
    "auto_install": False,
}
