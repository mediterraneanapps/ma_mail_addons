{
    "name": "Mail archives",
    "summary": """Adds menu to find old messages""",
    "category": "Discuss",
    "images": ['images/1.jpg'],
    "version": "12.0.1.0.1",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    'price': 13.33,
    'currency': 'EUR',

    "depends": [
        "mail",
    ],

    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    'installable': True,
}
