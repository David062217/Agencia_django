# Generated by Django 3.2.4 on 2021-06-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_rename_genero_choices_aspirante_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirante',
            name='genero',
            field=models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1),
        ),
    ]
