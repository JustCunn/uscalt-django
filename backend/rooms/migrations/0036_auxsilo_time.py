# Generated by Django 3.2.4 on 2021-11-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0035_auto_20211119_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='auxsilo',
            name='time',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
