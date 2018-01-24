# -*- coding: utf-8 -*-
from odoo import http

# class IgcsAprProd(http.Controller):
#     @http.route('/igcs_apr_prod/igcs_apr_prod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/igcs_apr_prod/igcs_apr_prod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('igcs_apr_prod.listing', {
#             'root': '/igcs_apr_prod/igcs_apr_prod',
#             'objects': http.request.env['igcs_apr_prod.igcs_apr_prod'].search([]),
#         })

#     @http.route('/igcs_apr_prod/igcs_apr_prod/objects/<model("igcs_apr_prod.igcs_apr_prod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('igcs_apr_prod.object', {
#             'object': obj
#         })