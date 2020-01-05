.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

=====================
 Multi-Brand Mailing
=====================

Mail-related stuff for multi-website support

* Makes following field in ``res.users`` website-dependent:

  * ``email``
  * ``signature``

* Makes following fields in ``mail.template`` website-dependent:

  * ``body_html``
  * ``mail_server_id``
  * ``report_template``

* Overrides ``mail.template``'s ``render_template`` method to add ``website``
  variable. It may cause incompatibility with other modules that redefine that
  method too.

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

     