# Generated by Django 4.2.1 on 2023-06-21 13:48
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_rol_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='apellido_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='apellido_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Apellido'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='nombre_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='nombre_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Nombre'),
        ),
    ]