# Generated by Django 3.2.4 on 2021-11-17 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0032_alter_roomlink_buyers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auxsilo',
            name='main_silo',
        ),
        migrations.RemoveField(
            model_name='auxsilo',
            name='owner',
        ),
    ]
