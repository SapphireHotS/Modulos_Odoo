#-*- encoding: utf-8 -*-
from odoo import api,fields,models

class software(models.Model):
    _name='software'
    _rec_name="nombre"
    idproducto=fields.Integer('ID producto', required=True)
    nombre=fields.Char('Nombre', required=True)
    precio=fields.Float('Precio')
    descripcion=fields.Text('Descripción')
    ultimaversion=fields.Many2one('versionsoftware','Última versión')

class clientes(models.Model):
    _name='clientes'
    _rec_name='cliente'
    idcliente=fields.Integer('ID Cliente', required=True)
    cliente=fields.Char('Nombre')
    apellidos=fields.Char('Apellidos')
    fechanac=fields.Date('Fecha nac', required=True)
    telefono=fields.Char('Teléfono')
    direccion=fields.Char('Dirección')
    





class hardware(models.Model):
    _name='hardware'
    _rec_name='nombre'
    idproducto=fields.Integer('ID producto', required=True)
    nombre=fields.Text('Nombre del producto', required=True)
    stock=fields.Integer('Stock actual', required=True)
    precio=fields.Float('Precio')
    descripcion=fields.Text('Descripción')
    

class versionsoftware(models.Model):
    _name='versionsoftware'
    _rec_name='revision'
    idversion=fields.Many2one('software', 'Versión', required=True)
    revision=fields.Char('Revisión', required=True)
    detalles=fields.Text('Detalles revisión')
    fecha=fields.Date('Fecha', required=True)
    idcliente=fields.Many2one('clientes','Cliente', require=True)

class departamentos(models.Model):
    _name='departamentos'
    _rec_name='nombredep'
    iddepartamento=fields.Integer('ID departamento', required=True)
    nombredep=fields.Char('Departamento', required=True)



class empleados(models.Model):
    _name='empleados'
    _rec_name='nombre'
    idempleado=fields.Integer('Identificador', required=True)
    nombre=fields.Char('Nombre', required=True)
    apellidos=fields.Char('Apellidos', required=True)
    dni=fields.Char('DNI', required=True)
    fechanac=fields.Date('Fecha de nacimiento', required=True)
    fechaalta=fields.Date('Fecha de alta',required=True)
    departamento=fields.Many2one('departamento', 'Departamento')