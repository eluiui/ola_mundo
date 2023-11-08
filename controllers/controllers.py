# -*- coding: utf-8 -*-
# from odoo import http


# class OlaMundo(http.Controller):
#     @http.route('/ola_mundo/ola_mundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ola_mundo/ola_mundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ola_mundo.listing', {
#             'root': '/ola_mundo/ola_mundo',
#             'objects': http.request.env['ola_mundo.ola_mundo'].search([]),
#         })

#     @http.route('/ola_mundo/ola_mundo/objects/<model("ola_mundo.ola_mundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ola_mundo.object', {
#             'object': obj
#         })
