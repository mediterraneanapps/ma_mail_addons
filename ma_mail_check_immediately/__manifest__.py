{
    'name': 'Check mail immediately',
    'version': '1.0.1',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    "category": "Discuss",
    "support": "mediterranean.apps@gmail.com",
    'price': 3.00,
    'currency': 'EUR',
    'depends': ['base', 'web', 'fetchmail', 'mail'],
    'data': [
        'views.xml',
    ],
    'qweb': [
        "static/src/xml/main.xml",
    ],
    'installable': False
}
