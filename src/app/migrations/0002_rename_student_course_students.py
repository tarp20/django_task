# Generated by Django 3.2.4 on 2021-06-23 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
    ]
