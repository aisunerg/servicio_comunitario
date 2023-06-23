# Generated by Django 4.2.1 on 2023-06-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_authuser_apellido_1_alter_authuser_apellido_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[(1, '-1'), (2, ('-1', '-2'))], max_length=2, verbose_name='Periodos del area')),
            ],
        ),
    ]