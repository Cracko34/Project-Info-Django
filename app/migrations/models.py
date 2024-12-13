from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    legajo = models.CharField(max_length=255)

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.CharField(max_length=255)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)