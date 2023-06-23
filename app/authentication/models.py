from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver


class Area(models.Model):
    nombre = models.CharField("Nombre del area", unique=True)

    def __str__(self):
        return self.nombre
    
class Tutores(models.Model):

    nombre_1 = models.CharField("Primer Nombre", max_length=50, blank=True, null=True)
    nombre_2 = models.CharField("Segundo Nombre", max_length=50, blank=True, null=True)
    apellido_1 = models.CharField("Primer Apellido", max_length=50, blank=True, null=True)
    apellido_2 = models.CharField("Segundo Apellido", max_length=50, blank=True, null=True)

    tipo_documentacion = models.CharField(max_length=1, choices=[("V", "Venezolano")], default="V")
    cedula = models.CharField("Cedula", max_length=8, unique=True, blank=True, null=True)

    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.nombre_1 +' '+ self.apellido_1

class Rol(models.Model):
    nombre = models.CharField("Nombre del rol administrativo", unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class AuthUser(AbstractUser):
    first_name = None
    last_name = None

    # username = models.CharField(max_length=255, blank=True, null=True)
    username = None

    nombre_1 = models.CharField("Primer Nombre", max_length=50)
    nombre_2 = models.CharField("Segundo Nombre", max_length=50)
    apellido_1 = models.CharField("Primer Apellido", max_length=50)
    apellido_2 = models.CharField("Segundo Apellido", max_length=50)

    # tipo_documentacion = models.CharField(max_length=1, blank=True, null=True)
    tipo_documentacion = models.CharField(max_length=4, choices=[("V", "Venezolano")], default="V")
    cedula = models.CharField("Cedula", max_length=8, unique=True)

    email = models.EmailField("Correo Electronico", unique=True, max_length=255)

    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    # create_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["tipo_documentacion", "cedula", "username"]

    objects = UserManager()

    def __str__(self):
        return "{} {}, C.I{}, Area: {}, Rol: {}".format(self.nombre_1, self.apellido_1, self.cedula, self.area, self.rol)


@receiver(pre_save, sender=AuthUser)
def delete_file_before(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(id=instance.id)

        if instance.password == obj.password:
            instance.set_password(obj.password)
        else:
            instance.set_password(instance.password)

    except:
        pass
