# -*- coding: utf-8 -*-
# from odoo import http


# class GestionActes(http.Controller):
#     @http.route('/gestion_actes/gestion_actes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_actes/gestion_actes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_actes.listing', {
#             'root': '/gestion_actes/gestion_actes',
#             'objects': http.request.env['gestion_actes.gestion_actes'].search([]),
#         })

#     @http.route('/gestion_actes/gestion_actes/objects/<model("gestion_actes.gestion_actes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_actes.object', {
#             'object': obj
#         })

