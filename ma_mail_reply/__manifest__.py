{
    "name": """Always show reply button""",
    "summary": """Got a message out of a Record? Now you can reply to it too!""",
    "category": "Discuss",
    "images": [],
    "version": "1.0.0",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 16.33,
    "currency": "EUR",

    "depends": [
        "ma_mail_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'templates.xml'
    ],
    "qweb": [
        "static/src/xml/reply_button.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
