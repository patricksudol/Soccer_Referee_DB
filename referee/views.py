from django.shortcuts import render, HttpResponse

from referee.models.referee import Referee

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

    
    career_totals = {
        'matches': matches.count(),
        'yellow_cards': '',
        'red_cards': '',
        'fouls': '',
        'penalties': ''
    }
    
    context['referee'] = referee
    context['matches'] = matches
    context['first_match'] = matches.first()
    context['last_match'] = matches.last()
    return render(request, 'referee.html', context)

"""
matches
Yellow Card Count
Red Card Count
Y Card / game
R Card / game
foul count
foul / game
penalties count
penalty / game
"""