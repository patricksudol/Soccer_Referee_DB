from django.db.models import Sum

from organization.models.match import Match
from sanction.models.card import YellowCard, RedCard
from sanction.models.penalty import Penalty


def referee_info(referee):
    debut = referee.first_match
    return {
        'name': referee.name_common,
        'total_assignments_count': referee.all_assignments.count(),
        'image_url': referee.image_url,
        'referee_url': '/referees/' + referee.referee_id,
        'debut_match': {
            'date': debut.match_date if debut else 'TBD',
            'home_team': debut.home_club.name if debut else '',
            'away_team': debut.away_club.name if debut else ''
        }
    }

def get_career_totals(referee):
    return (
        _referee_totals(referee) if referee.is_referee else _ar_totals(referee)
    )


def get_career_averages(referee, career_totals):
    return (
        _referee_averages(referee, career_totals) if referee.is_referee else {}
    )

def _referee_totals(referee):
    return {
        'centers': referee.referee_matches.count(),
        'fourths': referee.fourth_official_matches.count(),
        'yellow_cards': YellowCard.objects.filter(referee=referee).count(),
        'red_cards': RedCard.objects.filter(referee=referee).count(),
        'fouls': Match.objects.filter(referee=referee).aggregate(
            Sum('total_fouls')
        )['total_fouls__sum'],
        'penalties': Penalty.objects.filter(referee=referee).count()
    }


def _referee_averages(referee, career_totals):
    return {
        'yellow_cards': round(
            career_totals['yellow_cards'] / referee.referee_matches.count(), 
            2
        ),
        'red_cards': round(
            referee.referee_matches.count() / career_totals['red_cards'], 2
        ),
        'fouls': round(
            career_totals['fouls'] / referee.referee_matches.count(), 2
        ),
        'penalties': round(
            referee.referee_matches.count() / career_totals['penalties'], 2
        )
    }


def _ar_totals(referee):
    return {
        'total_assignments': referee.ar_assignments.count(),
        'ar1': referee.ar1_matches.count(),
        'ar2': referee.ar2_matches.count()
    }
