# Generated by Django 3.2 on 2023-04-25 15:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20230425_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='map_evento',
            field=ckeditor.fields.RichTextField(),
        ),
    ]