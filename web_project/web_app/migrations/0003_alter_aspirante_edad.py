# Generated by Django 3.2.4 on 2021-06-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20210608_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirante',
            name='edad',
            field=models.IntegerField(),
        ),
    ]