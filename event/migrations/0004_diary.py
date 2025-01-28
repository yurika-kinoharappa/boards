# Generated by Django 5.1.5 on 2025-01-23 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_study_textbook_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenki', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=1000)),
                ('hitokoto', models.CharField(max_length=100)),
                ('thank', models.CharField(max_length=300)),
            ],
        ),
    ]
