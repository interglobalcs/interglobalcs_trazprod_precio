# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class igcs_apr_prod(models.Model):
#     _name = 'igcs_apr_prod.igcs_apr_prod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100