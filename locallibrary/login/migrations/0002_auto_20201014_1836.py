# Generated by Django 3.1.2 on 2020-10-14 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='fecha_fallecimiento',
            new_name='fecha_fall',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='fecha_nacimiento',
            new_name='fecha_nac',
        ),
    ]