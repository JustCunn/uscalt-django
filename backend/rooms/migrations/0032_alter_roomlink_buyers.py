# Generated by Django 3.2.4 on 2021-11-17 20:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0031_roomlink_buyers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomlink',
            name='buyers',
            field=models.ManyToManyField(blank=True, default=None, related_name='mybuyers', to=settings.AUTH_USER_MODEL),
        ),
    ]
