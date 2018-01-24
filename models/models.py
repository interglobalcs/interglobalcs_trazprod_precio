# -*- coding: utf-8 -*-

from odoo import models, fields, api

class igcs_apr_prod(models.Model):
    _inherit = 'product.template'

    website_published = fields.Boolean('Visible in Website', copy=False, track_visibility='always')
