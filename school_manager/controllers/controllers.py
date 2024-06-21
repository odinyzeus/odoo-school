# -*- coding: utf-8 -*-
# from odoo import http


# class SatFactures(http.Controller):
#     @http.route('/sat_factures/sat_factures', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sat_factures/sat_factures/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sat_factures.listing', {
#             'root': '/sat_factures/sat_factures',
#             'objects': http.request.env['sat_factures.sat_factures'].search([]),
#         })

#     @http.route('/sat_factures/sat_factures/objects/<model("sat_factures.sat_factures"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sat_factures.object', {
#             'object': obj
#         })

