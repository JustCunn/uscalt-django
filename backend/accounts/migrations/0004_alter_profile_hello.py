# Generated by Django 3.2.4 on 2021-06-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hello',
            field=models.CharField(default='Hello', max_length=50),
        ),
    ]
