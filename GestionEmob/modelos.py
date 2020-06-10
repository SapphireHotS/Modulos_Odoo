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
    compras = fields.one2many('ventas','idventa', 'ventas')


class productos(models.Model):
    _name='productos'
    _rec_name= 'modelo'
    idproducto = fields.Char('ID del producto', required=True)
    modelo = fields.Char('Modelo', required=True)
    lugar = fields.Char('Lugar')
    estado = fields.Char('Estado')
    precio = fields.Float('Precio')



class stock(models.Model):
    _name='stock'
    idtienda = fields.Char('ID de la tienda', required=True)
    producto = fields.One2many('productos','modelo', 'Productos')


    
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



class ventas(models.Model):
    _name='ventas'
    _rec_name = 'idventa'
    idventa = fields.Char('ID de la venta', required=True)
    idproducto = fields.One2many('productos','modelo', 'Productos')
    idcliente = fields.Many2one('clientes', 'Cliente')
    fechaventa = fields.Date('Fecha de la venta', required=True)
