# Generated by Django 3.0.3 on 2020-02-08 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='avar_id',
            new_name='avar',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='fifth_official_id',
            new_name='fifth_official',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='var_id',
            new_name='var',
        ),
    ]