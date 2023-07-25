# -*- coding: utf-8 -*-
from odoo import api, fields, models
class ProductTemplate(models.Model):
    _inherit = 'product.template'
 
    name = fields.Char(string="Name", index='trigram', required=True,
                        store=True, translate=True, compute='_compute_NAME')

    @api.depends('make','model','year')
    def _compute_NAME(self):
        name_computed = ''
        for product in self:
            if product.detailed_type == 'motorcycle':
                if product.make != None:
                    name_computed += product.make
                if product.model != None:
                    name_computed += product.model
                if product.year != None:
                    name_computed += str(product.year)
                if name_computed != '':
                    product.name = name_computed
                else:
                    product.name = 'Unnamedmotorcycle'
            else:
                if product.name not in {'', None}:
                    product.name = product.name   
                else:
                    product.name = 'Unnamedproduct'     
