from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiantes, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

def curso(self):
    curso = Curso(nombre="Desarollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):


    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
        
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario= CursoFormulario()
    
    return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})






def profesores(request):

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
        
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])

            profesor.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario= ProfesorFormulario()
    
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def estudiantes(request):
    if request.method == "POST":

        miFormulario = EstudianteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
        
            estudiante = Estudiantes(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])

            estudiante.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario= EstudianteFormulario()
    
    return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})


def entregables(request):

    if request.method == "POST":

        miFormulario = EntregableFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
        
            entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"])

            entregable.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario= EntregableFormulario()
    
    return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario})


def buscar(request):

    if request.GET["camada"]:


        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        respuesta = "No enviaste datos"
    

    
    return render(respuesta, "AppCoder/inicio.html", {"respuesta":respuesta})

