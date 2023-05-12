from django.db import models
from authentication.models import AuthUser

class Project_SC(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=200, blank=True, null=True)
    tematica = models.CharField(max_length=200, blank=True, null=True)
    tutor = models.CharField(max_length=200, blank=True, null=True)
    periodo = models.CharField(max_length=200, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    coordinador = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True)


