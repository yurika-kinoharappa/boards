# Generated by Django 5.1.5 on 2025-01-25 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_diary_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='dd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2025, 1, 25))),
                ('jinbutu', models.CharField(max_length=400)),
                ('dekigoto', models.CharField(max_length=1000)),
                ('kansou', models.CharField(max_length=1000)),
            ],
        ),
    ]
