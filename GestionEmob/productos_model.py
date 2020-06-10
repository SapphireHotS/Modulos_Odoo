#-*- encoding: utf-8 -*-
from odoo import api,fields,models


class productos(models.Model):
    _name='productos'
    _rec_name= 'modelo'
    idproducto = fields.Char('ID del producto', required=True)
    modelo = fields.Char('Modelo', required=True)
    lugar = fields.Char('Lugar')
    estado = fields.Char('Estado')
    precio = fields.Float('Precio')
