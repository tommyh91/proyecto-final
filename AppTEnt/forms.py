from django import forms

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