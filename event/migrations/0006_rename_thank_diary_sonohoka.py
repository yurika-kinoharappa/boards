# Generated by Django 5.1.5 on 2025-01-23 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_diary_tenki'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='thank',
            new_name='sonohoka',
        ),
    ]
