from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Area, Rol, AuthUser
from django.contrib.auth.models import Group
from admin_interface.models import Theme

# Register your models here.
# admin.site.register(AuthUser)
# admin.site.register(Area)
# admin.site.register(Rol)
admin.site.unregister(Group)
admin.site.unregister(Theme)


@register(AuthUser)
class AuthUserAdmin(ModelAdmin):
    list_display = (
        "nombre_1",
        "nombre_2",
        "apellido_1",
        "apellido_2",
        "tipo_documentacion",
        "cedula",
        "area",
        "rol",
    )


@register(Rol)
class RolAdmin(ModelAdmin):
    list_display = ("nombre",)


@register(Area)
class AreaAdmin(ModelAdmin):
    list_display = ("nombre",)
