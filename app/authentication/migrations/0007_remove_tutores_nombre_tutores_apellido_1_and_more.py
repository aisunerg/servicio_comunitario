# Generated by Django 4.2.1 on 2023-06-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_tutores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutores',
            name='nombre',
        ),
        migrations.AddField(
            model_name='tutores',
            name='apellido_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Apellido'),
        ),
        migrations.AddField(
            model_name='tutores',
            name='apellido_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Apellido'),
        ),
        migrations.AddField(
            model_name='tutores',
            name='cedula',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='Cedula'),
        ),
        migrations.AddField(
            model_name='tutores',
            name='nombre_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Nombre'),
        ),
        migrations.AddField(
            model_name='tutores',
            name='nombre_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Nombre'),
        ),
        migrations.AddField(
            model_name='tutores',
            name='tipo_documentacion',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
