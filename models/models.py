# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Media(models.Model):
    _name = 'calculator.media'

    name = fields.Char(string="Media Type")
    cost = fields.Float()


class MediaRange(models.Model):
    _name = 'calculator.media_range'

    name = fields.Selection([('1-100', '1 - 100'),
                             ('101-200', '101 - 200'),
                             ('201-300', '201 - 300'),
                             ('301-400', '301 - 400'),
                             ('401-500', '401 - 500'),
                             ('501+', '501+')],
                            'Media Range (sqft)',
                            default='1-100'
                            )


class CustomerPrice(models.Model):
    _name = 'calculator.customer_price'

    name = fields.Selection([('client', 'Client'),
                             ('regular', 'Regular'),
                             ('ad', 'Ad')],
                            'Customer Type',
                            default='client')
    media = fields.Many2one('calculator.media', string='Media Type', required=True)
    range = fields.Selection([('1-100', '1 - 100'),
                             ('101-200', '101 - 200'),
                             ('201-300', '201 - 300'),
                             ('301-400', '301 - 400'),
                             ('401-500', '401 - 500'),
                             ('501+', '501+')],
                             'Media Range',
                             default='1-100')
    price = fields.Float()


class PrintCalculator(models.Model):
    _name = 'calculator.calc'

    client = fields.Selection([('client', 'Client'),
                               ('regular', 'Regular'),
                               ('ad', 'Ad')],
                              'Customer Type', default='client')
    media = fields.Many2one('calculator.media', string="Media Type", required=True)

