.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

=========
 Mailgun
=========

The module allows to receive incoming messages or send them to clients who uses external mail services (e.g. gmail.com) by using Mailgun.
There is no IMAP or POP3 servers on mailgun that is to be used with odoo.
That is why we need this module. It fetches messages from mailgun using their API and stores them in odoo.

TODO
====

* If emails are sent when odoo is stopped then Mailgun will retry (other than for delivery notification) during 8 hours at the following intervals before stop trying: 10 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 2 hour and 4 hours. This could be fixed by fetching undelivered messages after odoo starts.

Credits
=======

Contributors
------------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

     