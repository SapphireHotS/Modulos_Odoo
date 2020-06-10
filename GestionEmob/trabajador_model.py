#-*- encoding: utf-8 -*-
from odoo import api,fields,models


class trabajador(models.Model):
    _name='trabajador'
    idtrabajador = fields.Char('ID del trabajador', required=True)
    dni = fields.Char('DNI trabajador', required=True)
    usuario = fields.Char('Usuario')
    contrasenia = fields.Char('Contrasenia')
    nombre = fields.Char('Nombre trabajador')
    apellidos = fields.Char('Apellidos trabajador')
    numtelefono = fields.Char('Numero de telefono')
    correo = fields.Char('Correo electronico')