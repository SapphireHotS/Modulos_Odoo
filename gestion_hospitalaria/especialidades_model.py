#-*- encoding: utf-8 -*-

from odoo import api, fields, models

class especialidades(models.Model):
    _name= 'especialidades'
    name= fields.Char('Nombre', required=True)
    turno= fields.Char('Turno', required=True)
    active= fields.Boolean('Activa', default=True)
    consultas= fields.Char('Nº consultas', default=True)