from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido
        

def saludo(request): # primera vista
    
    p1 = Persona("Profesor Norberto","Diaz")

    # nombre = "Juan"
    # apellido = "Lopez"

    temasDelCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"] 

    ahora = datetime.datetime.now()
    
    # doc_externo = open("C:/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    # plt = Template(doc_externo.read())

    # doc_externo.close()

    # doc_externo = get_template('miplantilla.html')

    # ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso})

    # documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso})

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso})

def despedida(request): # primera vista

    return HttpResponse("Nos vemos gente")

def fechaEnTiempoReal(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html><body><h2>Fecha y hora actuales %s </h2></body></html>""" % fecha_actual
  
    return HttpResponse(documento)

def calcularEdad(request,edad,anio):

    #edadActual = 24
    periodo = anio - 2024
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2></body></html>" %(anio, edadFutura)

    return HttpResponse(documento)

def cursoDjango(request):

    fecha_actual = datetime.datetime.now()

    return render(request, "CursoDjango.html", {"fechaEnTiempoReal":fecha_actual})

def cursoCss(request):

    fecha_actual = datetime.datetime.now()

    return render(request, "CursoCss.html", {"fechaEnTiempoReal":fecha_actual})