# Generated by Django 4.2.1 on 2023-06-22 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_tutores'),
        ('biblioteca_SC', '0007_alter_project_sc_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_sc',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.tutores'),
        ),
    ]