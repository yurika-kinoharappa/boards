# Generated by Django 5.1.5 on 2025-01-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='peji1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='peji2',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
