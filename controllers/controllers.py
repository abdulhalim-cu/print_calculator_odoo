# -*- coding: utf-8 -*-
from odoo import http

class Calculator(http.Controller):
    @http.route('/calculator/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('calculator.index',{
            'sample_data': ['data 1', 'data 2', 'data 3'],
        })
