#la app tiene que recoger la información de los médicos que trabajan en la clínica. Formulario: información de contacto de cada médico, nombre, apellidos, dirección, teléfono, población, fecha nac, si está activo o no, sueldo bruto mensual y si participa o no en el servicio de urgencias. 
#Será necesario poder dar de alta los médicos, modificarlos si es necesario y darlos de baja, así como poder visualizarlos en forma de lista. Para acceder a esta app se deberá entrar en el menú Gestión_Hospitalaria.



#-*- encoding: utf-8 -*-
{
    'name': 'Gestión Hospitalaria',
    'description': 'Gestión Hospitalaria',
    'author': 'Valentin',
    'depends': ['mail'],
    'data': ['medicos_view.xml','especialidades_view.xml', 'camas_view.xml','pacientes_view.xml', 'consultas_view.xml', 'ingresos_view.xml','qweb001.xml'],
    'application': True,   
}