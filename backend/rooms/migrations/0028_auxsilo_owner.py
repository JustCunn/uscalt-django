# Generated by Django 3.2.4 on 2021-11-14 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0027_auxsilo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='auxsilo',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='aux_silo', to=settings.AUTH_USER_MODEL),
        ),
    ]
