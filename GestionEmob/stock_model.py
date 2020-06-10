#-*- encoding: utf-8 -*-
from odoo import api,fields,models


class stock(models.Model):
    _name='stock'
    idtienda = fields.Char('ID de la tienda', required=True)
    producto = fields.One2many('productos', 'Productos')