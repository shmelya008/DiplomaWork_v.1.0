# Generated by Django 5.1.3 on 2024-11-15 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HAStudio', '0002_alter_post_publish_alter_user_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2024, 11, 15, 16, 51, 37, 228828, tzinfo=datetime.timezone.utc)),
        ),
    ]
