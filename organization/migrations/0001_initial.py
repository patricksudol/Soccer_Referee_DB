# Generated by Django 3.0.3 on 2020-02-07 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('club_id', models.CharField(max_length=4)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_clubs', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_clubs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('season', models.IntegerField()),
                ('date_begin', models.DateField(blank=True, null=True)),
                ('date_end_reg', models.DateField(blank=True, null=True)),
                ('date_begin_playoffs', models.DateField(blank=True, null=True)),
                ('date_end_playoffs', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_seasons', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_seasons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('match_id', models.CharField(max_length=12)),
                ('match_date', models.DateField()),
                ('week', models.IntegerField(blank=True, null=True)),
                ('day', models.CharField(blank=True, choices=[('U', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('H', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], max_length=1, null=True)),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('result', models.CharField(choices=[('H', 'Home'), ('D', 'Draw'), ('A', 'Away')], max_length=1)),
                ('stage', models.CharField(blank=True, max_length=10, null=True)),
                ('leg', models.IntegerField(blank=True, null=True)),
                ('total_fouls', models.IntegerField(default=0)),
                ('home_fouls', models.IntegerField(default=0)),
                ('away_fouls', models.IntegerField(default=0)),
                ('total_cards_yellow', models.IntegerField(default=0)),
                ('home_cards_yellow', models.IntegerField(default=0)),
                ('away_cards_yellow', models.IntegerField(default=0)),
                ('total_cards_red', models.IntegerField(default=0)),
                ('home_cards_red', models.IntegerField(default=0)),
                ('away_card_red', models.IntegerField(default=0)),
                ('total_penalties', models.IntegerField(default=0)),
                ('home_penalties', models.IntegerField(default=0)),
                ('away_penalties', models.IntegerField(default=0)),
                ('ar1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar1_matches', to='referee.Referee')),
                ('ar2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar2_matches', to='referee.Referee')),
                ('avar_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avar_matches', to='referee.Referee')),
                ('away_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='organization.Club')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_matchs', to=settings.AUTH_USER_MODEL)),
                ('fifth_official_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_official_matches', to='referee.Referee')),
                ('fourth_official', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_official_matches', to='referee.Referee')),
                ('home_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='organization.Club')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_matchs', to=settings.AUTH_USER_MODEL)),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referee_matches', to='referee.Referee')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Season')),
                ('var_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='var_matches', to='referee.Referee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
