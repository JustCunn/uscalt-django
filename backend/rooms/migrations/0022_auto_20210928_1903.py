# Generated by Django 3.2.4 on 2021-09-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0021_auto_20210926_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxsilo',
            name='data',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='auxsilo',
            name='main_silo',
            field=models.ManyToManyField(blank=True, default=None, related_name='data', to='rooms.MainSilo'),
        ),
        migrations.AlterField(
            model_name='mainsilo',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
