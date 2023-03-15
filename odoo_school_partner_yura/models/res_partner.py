from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def check_reception_time(self):
        for rec in self:
            result = self.env['res.partner'].search([
                ('email', '=', rec.email),
                ('id', '!=', rec.id),
            ])
            if result:
                raise ValidationError(_('This email is already registered'))
