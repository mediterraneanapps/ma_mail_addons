{
    'name': 'Mail Relocation',
    'version': '11.0.1.0.6',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Discuss',
    'images': ['images/m1.png'],
    "support": "mediterranean.apps@gmail.com",
    'price': 33.33,
    'currency': 'EUR',
    'depends': [
        'ma_mail_all',
    ],
    'data': [
        'mail_move_message_views.xml',
        'data/mail_move_message_data.xml',
    ],
    'qweb': [
        'static/src/xml/mail_move_message_main.xml',
    ],
    'installable': False,
}
