from django.db.models import Sum
from django.shortcuts import render

from organization.models.match import Match
from referee.models.referee import Referee
from sanction.models.card import YellowCard, RedCard
from sanction.models.penalty import Penalty


def referees(request):
    context = {}
    refs = Referee.objects.all().order_by('name_family')
    counter = 1
    referees_list = []
    for ref in refs:
        all = ref.all_assignments
        debut = all.order_by('match_date').first() if all else ''
        ref_dict = {
            'name': ref.name_common,
            'total_assignments_count': all.count(),
            'image_url': ref.image_url,
            'referee_url': '/referees/' + ref.referee_id,
            'debut_match': {
                'date': debut.match_date if debut else 'TBD',
                'home_team': debut.home_club.name if debut else '',
                'away_team': debut.away_club.name if debut else ''
            },
            'count': counter,
            'first_in_row': True if counter % 4 == 1 else False
        }
        referees_list.append(ref_dict)
        counter += 1
    context['referees'] = referees_list
    context['nbar'] = 'referees'
    return render(request, 'referees.html', context)

def referee_bio(request, referee_id):
    referee = Referee.objects.get(referee_id=referee_id)
    matches = referee.all_assignments.all().order_by('match_date')
    context = {}

    is_referee = bool(referee.referee_matches.count())
    
    if is_referee:
        career_totals = {
            'centers': referee.referee_matches.count(),
            'fourths': referee.fourth_official_matches.count(),
            'yellow_cards': YellowCard.objects.filter(referee=referee).count(),
            'red_cards': RedCard.objects.filter(referee=referee).count(),
            'fouls': Match.objects.filter(referee=referee).aggregate(Sum('total_fouls'))['total_fouls__sum'],
            'penalties': Penalty.objects.filter(referee=referee).count()
        }
    else:
        career_totals = {
            'total_assignments': referee.ar_assignments.count(),
            'ar1': referee.ar1_matches.count(),
            'ar2': referee.ar2_matches.count()
        }

    if is_referee:
        career_averages = {
            'yellow_cards': round(career_totals['yellow_cards'] / referee.referee_matches.count(), 2),
            'red_cards': round(referee.referee_matches.count() / career_totals['red_cards'], 2),
            'fouls': round(career_totals['fouls'] / referee.referee_matches.count(), 2),
            'penalties': round(referee.referee_matches.count() / career_totals['penalties'], 2)
        }
    else:
        career_averages = {
            'yellow_cards': 0,
            'red_cards': 0,
            'fouls': 0,
            'penalties': 0
        }

    print(career_averages['yellow_cards'])
    
    context['referee'] = referee
    context['matches'] = matches
    context['first_match'] = matches.first()
    context['last_match'] = matches.last()
    context['career_totals'] = career_totals
    context['career_averages'] = career_averages
    return render(request, 'referee.html', context)
