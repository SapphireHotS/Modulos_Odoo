#-*- encoding: utf-8 -*-
from odoo import api,fields,models


class clientes(models.Model):
    _name='clientes'
    _rec_name= 'nombre'
    dni = fields.Char('DNI cliente', required=True)
    usuario = fields.Char('Usuario cliente')
    contrasenia = fields.Char('Contrasenia cliente')
    nombre = fields.Char('Nombre del cliente')
    apellidos = fields.Char('Apellidos del cliente')
    numtelefono = fields.Char('Telefono del cliente')
    #compras = fields.one2many('ventas', 'ventas')
