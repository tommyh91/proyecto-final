from django.db import models

# Create your models here.

class alumno(models.Model):
    def __str__(self):
        return f"¨{self.nombre}"
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()

class curso(models.Model):

    def __str__(self):
        return f"¨{self.nombre_curso}"
    nombre_curso = models.CharField(max_length=50)
    numero_comision = models.IntegerField()
    

class entrega(models.Model):
    def __str__(self):
        return f"¨{self.nombre_proyecto}"
    nombre_proyecto = models.CharField(max_length=50)
    fecha_entrega = models.DateField()