# Generated by Django 3.2.4 on 2021-12-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0039_roomlink_off_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomlink',
            name='data_needed',
            field=models.BooleanField(default=False),
        ),
    ]
