# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class igcs_apr_prod(models.Model):
    _inherit = 'product.template'

    website_published = fields.Boolean('Visible in Website', copy=False, track_visibility='onchange')
    list_price = fields.Float(
        'Sales Price', default=1.0,
        digits=dp.get_precision('Product Price'),
        help="Base price to compute the customer price. Sometimes called the catalog price.", track_visibility='onchange')
