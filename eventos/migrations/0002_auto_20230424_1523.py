# Generated by Django 3.2 on 2023-04-24 20:23

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='fecha_actualizacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de actualización'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]