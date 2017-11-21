from django.db import models
from django.contrib import admin

# Create your models here.
class Alumno(models.Model):
    nombre  = models.CharField(max_length=30)
    edad = models.IntegerField()
    carnet = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Profesor (models.Model):
    nombre =   models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    salario = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Nota (models.Model):
    total    = models.CharField(max_length=5)
    zona    = models.CharField(max_length=4)
    final    = models.CharField(max_length=4)
    curso = models.ForeignKey(Curso)
    alumno = models.ForeignKey(Alumno)
    encargado = models.ForeignKey(Profesor)

    def __str__(self):
        return self.total

class Grado(models.Model):
    nombre  = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    materias   = models.ManyToManyField(Materia, through='Pensum')

    def __str__(self):
        return self.nombre


class Pensum (models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class PensumInLine(admin.TabularInline):
    model = Pensum
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (PensumInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (PensumInLine,)
