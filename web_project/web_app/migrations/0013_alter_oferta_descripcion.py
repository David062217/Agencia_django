# Generated by Django 3.2.4 on 2021-07-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0012_alter_profesion_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
