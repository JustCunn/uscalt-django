# Generated by Django 3.2.4 on 2021-09-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20210919_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomlink',
            name='android',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='roomlink',
            name='ios',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='roomlink',
            name='web',
            field=models.BooleanField(default=False),
        ),
    ]
