# Generated by Django 5.1.5 on 2025-01-27 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_diet_play_diet_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
