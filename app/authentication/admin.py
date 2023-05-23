from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Area, Rol, AuthUser

# Register your models here.
admin.site.register(AuthUser)
admin.site.register(Area)
admin.site.register(Rol)
