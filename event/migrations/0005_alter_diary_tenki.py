# Generated by Django 5.1.5 on 2025-01-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='tenki',
            field=models.CharField(default='記録なし', max_length=50),
        ),
    ]
