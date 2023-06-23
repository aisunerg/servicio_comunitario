# Generated by Django 4.2.1 on 2023-06-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_tutores'),
        ('biblioteca_SC', '0008_alter_project_sc_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_sc',
            name='tutor',
        ),
        migrations.AddField(
            model_name='project_sc',
            name='tutor',
            field=models.ManyToManyField(blank=True, null=True, to='authentication.tutores'),
        ),
    ]
