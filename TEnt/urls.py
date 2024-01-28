"""
URL configuration for TEnt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppTEnt.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", inicio, name= "inicio"),
    path("alumnos", ver_alumno, name="alumnos"),
    path("cursos", ver_curso, name= "cursos"),
    path("entregas", ver_entrega, name="entregas"),

    #URLs forms
    path("nuevo_alumno", agregar_alumno),
    path("nuevo_curso", agregar_curso, name="nuevo_curso"),
    path("nueva_entrega", agregar_entrega),

    #URLs buscar pelis
    path("buscar_añoalumno", busqueda_alumnoxaño),
    path("resultadoalumno/", resultado_buscar_alumno_por_año),


# URL de actualizacion
    path("update_curso/<nombre_curso>", actualizar_curso, name="Actualizar curso"),

#URL para eliminar
    path("eliminarCurso/<nombre_curso>", eliminar_curso, name= "Eliminar Curso"),

#URL lista de pelis con class
    path("listaAlumno", lista_alumno.as_view(), name="Lista Alumnos"),
    path("CrearAlumno", crear_alumnos.as_view(), name="Crear Alumnos"),
    path("ActualizarAlumno/<int:pk>", actualizar_alumnos.as_view(), name="Actualizar Alumnos"),
    path("BorrarAlumno/<int:pk>", eliminar_alumnos.as_view(), name="Eliminar Alumnos"),

    ]







"""path("NuevoAlumno/", agregar_alumno),
path("NuevoCurso/", agregar_curso),"""

