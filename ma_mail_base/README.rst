===========
 Mail Base
===========

* makes built-in mail js features extendable.
* handles ``search_default_*`` parameters in context.
* fixes toggling left bar
* fixes Recipients field. Out-of-box this field could be empty.

One can say, that the module do this todo from `addons/mail/static/src/js/chat_manager.js <https://github.com/odoo/odoo/blob/9.0/addons/mail/static/src/js/chat_manager.js#L57>`__

    // to do: move this to mail.utils

Note. Due to odoo restrictions, module makes mail initialization again. That is browser loads emoji and other chat data twice. This is the only way to make Mail feature extendable.

Credits
=======

Contributors
------------
* Mediterranean Apps<mediterranean.apps@gmail.com>__

Sponsors
--------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__
