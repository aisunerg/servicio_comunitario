from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils import timezone
from django.db import models


class Area(models.Model):
    nombre = models.CharField("Nombre del area",unique=True, blank=True, null=True)

    def __str__(self):
        return self.nombre 
    
class Rol(models.Model):
    nombre = models.CharField("Nombre del rol administrativo", unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.nombre 



class AuthUser(AbstractUser):
    first_name = None
    last_name = None
    
    username = models.CharField(max_length=255, blank=True, null=True)
    
    nombre_1 = models.CharField(max_length=50, blank=True, null=True)
    nombre_2 = models.CharField(max_length=50, blank=True, null=True)
    apellido_1 = models.CharField(max_length=50, blank=True, null=True)
    apellido_2 = models.CharField(max_length=50, blank=True, null=True)
    
    tipo_documentacion = models.CharField(max_length=1, blank=True, null=True)
    cedula = models.CharField("Cedula", max_length=8, unique=True, blank=True, null=True)
    
    email = models.EmailField('Correo Electronico', unique=True, max_length=255, blank=True, null=True)
    
    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.SET_NULL)
    rol = models.ForeignKey(Rol, blank=True, null=True, on_delete=models.SET_NULL)
    

    # create_date = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ["tipo_documentacion","cedula", "username"]
    
    objects = UserManager()
    
    def __str__(self):
        return "{} {}, C.I{}, Area: {}, Rol: {}".format(self.nombre_1,self.apellido_1,self.cedula, self.area, self.rol)
    
    
