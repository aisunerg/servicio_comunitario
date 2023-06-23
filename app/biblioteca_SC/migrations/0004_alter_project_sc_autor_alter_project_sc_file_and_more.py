# Generated by Django 4.2.1 on 2023-06-22 15:41

import django.core.validators
from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_SC', '0003_alter_project_sc_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_sc',
            name='autor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='file',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='./projects', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'])]),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='periodo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='tematica',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='tipo_proyecto',
            field=models.CharField(choices=[('SC', 'Servicio Comunitario'), ('PreG', 'Pre-Grado'), ('PosG', 'Post-Grado')], default='SC', max_length=4),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='tutor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project_sc',
            name='ubicacion_servicio',
            field=models.CharField(max_length=200),
        ),
    ]