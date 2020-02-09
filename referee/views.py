from django.shortcuts import render

from referee.models.referee import Referee

def referees(request):
    context = {}
    refs = Referee.objects.all().order_by('name_family')[:10]
    counter = 1
    referees_list = []
    for ref in refs:
        all = ref.all_assignments
        debut = all.order_by('match_date').first() if all else ''
        ref_dict = {
            'name': ref.name_common,
            'total_assignments_count': all.count(),
            'image_url': ref.image_url,
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

