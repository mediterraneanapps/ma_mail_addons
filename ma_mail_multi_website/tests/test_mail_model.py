from odoo import models, fields


class MailTest(models.Model):
    _inherit = 'mail.test.simple'

    company_id = fields.Many2one('res.company', default=lambda self: self.env['res.company']._company_default_get())
    website_id = fields.Many2one('website', default=lambda self: self.env['website'].browse(self.env.context.get('website_id')))
