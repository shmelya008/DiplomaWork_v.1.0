# Generated by Django 5.1.3 on 2024-11-20 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HAStudio', '0011_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2024, 11, 20, 16, 33, 15, 633909)),
        ),
    ]
