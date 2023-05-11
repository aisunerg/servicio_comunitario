from django.db import models

# Create your models here.
class Usuario():
    nombre = models.CharField(max_length=50)
    nombre_2 = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido_2 = models.CharField(max_length=50)
    cedula = models.CharField(max_length=8)
    area = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    tipo_documentacion = models.CharField(max_length=3)


class Project_SC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    tematica = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    coordinador = models.ForeignKey(Usuario)


