from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import *
from AppTEnt.forms import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def inicio(request):

    return render(request, "AppTEnt/inicio.html")

def ver_alumno(request):
    
    mis_alumnos = alumno.objects.all()

    info = {"alumnos":mis_alumnos}

    return render(request, "AppTEnt/alumnos.html", info)



def ver_curso(request):
    
    mis_cursos = curso.objects.all()

    info = {"Cursos":mis_cursos}

    return render(request, "AppTEnt/cursos.html", info)

def ver_entrega(request):
    
    mis_entregas = entrega.objects.all()

    info = {"Entregas":mis_entregas}

    return render(request, "AppTEnt/entregas.html", info)

def agregar_alumno(request):

    # Sbaer que el usuario da click en guardar
    
    if request.method == "POST":
        
        nuevo_formulario = AlumnoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            alumno_nuevo = alumno(nombre=info["nombre"], apellido=info["apellido"], mail=info["mail"])
            
            alumno_nuevo.save()

            return render(request, "AppTEnt/inicio.html")

    else:
        nuevo_formulario = AlumnoFormulario()

    return render(request, "AppTEnt/formuAlumno.html", {"mi_formu_alumno":nuevo_formulario})


def agregar_curso(request):

    # Sbaer que el usuario da click en guardar
    
    if request.method == "POST":
        
        nuevo_formulario = CursoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            curso_nuevo = curso(nombre_curso=info["nombre_curso"], numero_comision=info["numero_comision"])
            
            curso_nuevo.save()

            return render(request, "AppTEnt/inicio.html")

    else:
        nuevo_formulario = CursoFormulario()

    return render(request, "AppTEnt/formucurso.html", {"mi_formu_curso":nuevo_formulario})

def agregar_entrega(request):

    # Sbaer que el usuario da click en guardar
    
    if request.method == "POST":
        
        nuevo_formulario = EntregaFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data

            entrega_nueva = entrega(nombre_proyecto=info["nombre_proyecto"], fecha_entrega=info["fecha_entrega"])
            
            entrega_nueva.save()

            return render(request, "AppTEnt/inicio.html")

    else:
        nuevo_formulario = EntregaFormulario()

    return render(request, "AppTEnt/formuentrega.html", {"mi_formu_entrega":nuevo_formulario})


def busqueda_alumnoxaño(request):
    
    return render(request, "AppTEnt/busqueda_alumnoxaño.html")


def resultado_buscar_alumno_por_año(request):

    if request.method=="GET":

        año = request.GET("año")

        resultado_alumno = alumno.objects.filter(año__icontains=año)

    return render(request, "AppTEnt/busqueda_alumnoxaño")


# Actualizar Curso
def actualizar_curso(request, nombre_curso):

    # que serie quiero actualizar?
    curso_escogido = curso.objects.get(nombre_curso=nombre_curso)


    if request.method == "POST":
        
        nuevo_formulario = CursoFormulario(request.POST)

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data
            # aca estan los datos a actualizar, si borro uno de aca no se actualiza
            curso_escogido.nombre_curso = info["nombre_curso"]
            curso_escogido.numero_comision = info["numero_comision"]

            curso_escogido.save()

            return render(request, "AppTEnt/inicio.html")

    else: #con el initial= aparece la info en el cuadradito
        nuevo_formulario = CursoFormulario(initial={"nombre_curso":curso_escogido.nombre_curso,
                                                    "numero_comision":curso_escogido.numero_comision})

    return render(request, "AppTEnt/update_curso.html", {"mi_formu_curso":nuevo_formulario})


# BORRAR Cursos

def eliminar_curso(request, nombre_curso):

    # que serie quiero borrar?
    curso_escogido = curso.objects.get(nombre_curso=nombre_curso)

    curso_escogido.delete()
    
    return render(request, "AppTEnt/cursos.html")


#CRUD DE ALUMNOS (BASADO EN CLASS)

#R de read from list view (importar)

class lista_alumno(ListView):

    model = alumno
#para que esto funque, tiene que estar si o si en el nombre del model y desp "_list" el html
    #sino habria que agregar esto

#CREAR ALUMNOS

class crear_alumnos(CreateView):
    model = alumno
    template_name = "AppTEnt/crearAlumnos.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = "/listaAlumno"


#Update de alumnos
    
class actualizar_alumnos(UpdateView):
    model = alumno
    template_name = "AppTEnt/crearAlumnos.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = "/listaAlumno"

#Delete
class eliminar_alumnos(DeleteView):
    model = alumno
    template_name = "AppTEnt/BorrarAlumnos.html"
    success_url = "/listaAlumno"



""" AGREGAR ALUMNO CON html
def agregar_alumno(request):

    # Sbaer que el usuario da click en guardar
    if request.method == "POST":

        alumno_nuevo = alumno(
            nombre=request.POST["nombre"],
            apellido=request.POST["appellido"] ,
            mail=request.POST["mail"]
            )

        alumno_nuevo.save()
    return render(request, "AppTEnt/nuevo_alumno.html")

"""









"""
def agregar_curso(request):
    curso1 = curso(nombre_curso = "Excel", numero_comision = 14)
    curso1.save()

    return HttpResponse("Se agrego una curso..")"""