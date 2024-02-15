from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlumnoFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    mail=forms.EmailField()


class CursoFormulario(forms.Form):
    nombre_curso = forms.CharField()
    numero_comision = forms.IntegerField()


class EntregaFormulario(forms.Form):
    nombre_proyecto = forms.CharField(max_length=50)
    fecha_entrega = forms.DateField()






# TODO ESTO DE ABAJO SI QUISIERA ELEGIR LOS CAMPOS A CREAR
"""
class Registrarusuario(UserCreationForm):
    email = forms.EmailField(label="correo electronico")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repita su contraseña", widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]"""