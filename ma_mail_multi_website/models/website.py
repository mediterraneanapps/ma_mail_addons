from odoo import models, fields


class Website(models.Model):
    _inherit = "website"

    mail_server_id = fields.Many2one('ir.mail_server', 'Outgoing Mails', help='Default outgoing mail server')
