# Generated by Django 3.2.4 on 2021-09-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0025_alter_roomlink_main_silo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomlink',
            name='main_silo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_link', to='rooms.mainsilo'),
        ),
    ]
