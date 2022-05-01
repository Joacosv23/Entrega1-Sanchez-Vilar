from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader



def saludo(request):
    return HttpResponse("Hola Django-Coder")


def probandoTemplate(self):

    nom = "Nicolas"
    ap = "Perez"

    diccionario = {"nombre": nom, "apellido": ap,}

    #miHtml = open("C:/Users/joaco/OneDrive/Documentos/Entrega1 Sanchez Vilar/Proyecto1/plantillas/template1.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(diccionario)

    #documento = plantilla.render(miContexto)

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

