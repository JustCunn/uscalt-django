# Generated by Django 3.2.4 on 2021-07-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_roomlink_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomlink',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='rooms.room'),
        ),
    ]
