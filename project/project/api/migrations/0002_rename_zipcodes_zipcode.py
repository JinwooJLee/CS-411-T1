# Generated by Django 3.2.3 on 2021-12-13 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ZipCodes',
            new_name='ZipCode',
        ),
    ]
