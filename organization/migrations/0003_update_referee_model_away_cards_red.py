# Generated by Django 3.0.3 on 2020-02-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_update_referee_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='away_card_red',
            new_name='away_cards_red',
        ),
    ]
