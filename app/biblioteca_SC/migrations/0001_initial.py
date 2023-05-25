# Generated by Django 4.2.1 on 2023-05-23 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_SC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('autor', models.CharField(blank=True, max_length=200, null=True)),
                ('tematica', models.CharField(blank=True, max_length=200, null=True)),
                ('tutor', models.CharField(blank=True, max_length=200, null=True)),
                ('periodo', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='./projects')),
                ('coordinador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
