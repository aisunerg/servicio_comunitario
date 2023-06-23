# Generated by Django 4.2.1 on 2023-06-23 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_authuser_tipo_documentacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutores',
            options={'verbose_name': 'Tutor', 'verbose_name_plural': 'Tutores'},
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, verbose_name='Nombre del area')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.area')),
            ],
        ),
    ]
