{
    "name": """Show message recipients""",
    "summary": """Allows you be sure, that all discussion participants were notified""",
    "category": "Discuss",
    "images": ['images/1.png'],
    "version": "12.0.1.0.1",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 16.00,
    "currency": "EUR",

    "depends": [
        'mail',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'templates.xml',
    ],
    "qweb": [
        'static/src/xml/recipient.xml',
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
