# Generated by Django 3.2.4 on 2022-01-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0041_roomlink_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomlink',
            name='sample',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
