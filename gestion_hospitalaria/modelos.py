#-*- encoding: utf-8 -*-
#especialidad, medico, paciente, consultas 
# Vistas: alta pacientes (asignar médico), buscar/ver pacientes, ingresos de pacientes en camas, informes (imprimir si me da la gana)
from odoo import api, fields, models

class medicos(models.Model):
    _name= 'medicos'
    _rec_name='name'
    name= fields.Char('Nombre', required=True)
    apellidos= fields.Char('Apellidos', required=True)
    direccion= fields.Char('Dirección')
    telefono= fields.Char('Teléfono', required=True)
    poblacion= fields.Char('Población')
    fechanac=fields.Date('Fecha de nacimiento')
    activo=fields.Boolean('Activo', default=True)
    sueldo=fields.Float('Sueldo bruto mensual')
    participaUrgencias= fields.Boolean('Participa en urgencias', default=True)
    especialidad=fields.Many2one('especialidades','Especialidad')

class especialidades(models.Model):
    _name= 'especialidades'
    _rec_name='name'
    name= fields.Char('Nombre', required=True)
    turno= fields.Selection([('Mañana','Tarde')], default='Mañana')
    active= fields.Boolean('Activa', default=True)
    consultas= fields.Integer('Nº consultas', required=True)
    descripcion= fields.Text('Descripción')

class camas(models.Model):
    _name= 'camas'
    _rec_name='identificador'
    identificador=fields.Char('Identificador cama', required=True)
    active=fields.Boolean('¿Ocupada?', default=False)

class pacientes(models.Model):
    _name='pacientes'
    _rec_name='nombre'#crea un identificador para la tabla.
    nombre= fields.Char('Nombre', required=True)
    apellidos=fields.Char('Apellidos', required=True)
    telefono= fields.Char('Teléfono', required=True)
    nss=fields.Char('Número Seguridad Social', required=True)
    familiar=fields.Char('Teléfono familiar para contacto', required=True)
    poblacion= fields.Char('Población')
    profesion=fields.Char('Profesión')
    fechanac=fields.Date('Fecha de nacimiento')
    medico=fields.Many2one('medicos.medicos')

class consultas(models.Model):
    _name='consultas'
    _rec_name='numConsulta'
    numConsulta=fields.Integer('Número de consulta', required=True)
    medico=fields.Many2one('medicos.medicos')
    tipo=fields.Many2one('especialidades','Especialidad')



class ingresos(models.Model):
    _name='ingresos'
    _rec_name='identificador'
    identificador=fields.Integer('Identificador', required=True)
    medico=fields.Many2one('medicos','Médico', required=True)
    paciente=fields.Many2one('pacientes','Paciente', required=True)
    cama=fields.Many2one('camas.camas', required=True)
    especialidad=fields.Many2one('especialidades', 'Especialidad', required=True)
    diagnostico=fields.Char('Diagnóstico', required=True)
    tratamiento=fields.Char('Tratamiento', required=True)
    descripcion=fields.Char('Descripción')
    fecha_alta=fields.Date('Fecha alta', required=True)
    fecha_baja=fields.Date('Fecha baja', required=True)

#class Operaciones(models.Model):
#    _name='operaciones'
#    _rec_name='identificador'
#    identificador=fields.Char('Identificador', required=True)
#    paciente_id=fields.Many2one('pacientes','Paciente')
#    medico_id=fields.Many2one('medicos','Médico')
#    quirofano=fields.Char('Quirófano', required=True)
#    fecha=fields.Date('Fecha', required=True)
#    intervención=fields.Char('Intervención quirúrgica', required=True)
#    notas=fields.Text('Notas')