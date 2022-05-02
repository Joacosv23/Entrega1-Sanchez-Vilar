from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=40)

class EstudianteFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    fechaDeEntrega= forms.DateField()
    entregado = forms.BooleanField()