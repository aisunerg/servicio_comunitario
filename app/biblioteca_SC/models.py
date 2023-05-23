from django.db import models


from authentication.models import AuthUser
from gdstorage.storage import GoogleDriveStorage

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .utils.tranfers_owner import get_id_from_url, get_drive_service, change_file_settings, delete_file

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Project_SC(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=200, blank=True, null=True)
    tematica = models.CharField(max_length=200, blank=True, null=True)
    tutor = models.CharField(max_length=200, blank=True, null=True)
    periodo = models.CharField(max_length=200, blank=True, null=True)

    area = models.CharField(max_length=200, blank=True, null=True)

    coordinador = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, blank=True, null=True)

    file = models.FileField(upload_to="./projects", storage=gd_storage, blank=True, null=True)


@receiver(post_save, sender=Project_SC)
def transferring_ownership(sender, instance, **kwargs):
    file_id = get_id_from_url(instance.file.url)
    service = get_drive_service()
    change_file_settings(service, file_id)


@receiver(post_delete, sender=Project_SC)
def transferring_ownership(sender, instance, **kwargs):
    file_id = get_id_from_url(instance.file.url)
    service = get_drive_service()
    delete_file(service, file_id)
