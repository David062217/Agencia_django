# Generated by Django 3.2.4 on 2021-06-28 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_rename_descrpcion_oferta_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='fecha_fin',
        ),
    ]
