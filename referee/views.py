from django.core.paginator import Paginator
from django.shortcuts import render

from referee.models import Referee
from referee.utils.career_totals import (
    get_career_averages, get_career_totals, referee_info
)
from sanction.models import Penalty,RedCard, YellowCard


def referees(request, page_number):
    referees = Referee.objects.all().order_by('name_family')
    referees_list = []
    paginator = Paginator(referees, 12)
    counter = 1
    for referee in paginator.object_list:
        ref_dict = referee_info(referee)
        ref_dict.update(
            {
                'count': counter,
                'first_in_row': True if counter % 4 == 1 else False
            }
        )
        referees_list.append(ref_dict)
        counter += 1
    paginator = Paginator(referees_list, 12)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':  page_obj,
        'page_range': paginator.page_range,
        'current_page_number': page_number,
        'nbar': 'referees'
    }
    return render(request, 'referees.html', context)


def referee_bio(request, referee_id):

    referee = Referee.objects.get(referee_id=referee_id)
    matches = referee.all_assignments.all().order_by('match_date')

    match_list = []
    for match in matches:
        match_dict = {
            'match_id': match.match_id,
            'match_date': match.match_date,
            'match_position': match.referee_position(referee),
            'home_club_name': match.home_club.name,
            'home_score': match.home_score,
            'home_fouls': match.home_fouls,
            'home_cards_yellow': match.home_cards_yellow,
            'home_cards_red': match.home_cards_red,
            'home_penalties': match.home_penalties,
            'away_club_name': match.away_club.name,
            'away_score': match.away_score,
            'away_fouls': match.away_fouls,
            'away_cards_yellow': match.away_cards_yellow,
            'away_cards_red': match.away_cards_red,
            'away_penalties': match.away_penalties,
            'yellow_cards': YellowCard.objects.filter(match=match),
            'red_cards': RedCard.objects.filter(match=match),
            'penalties': Penalty.objects.filter(match=match),
            'is_sanction': bool(match.yellowcard_set.all() or match.redcard_set.all() or match.penalties.all())
        }
        match_list.append(match_dict)

    career_totals = get_career_totals(referee)
    career_averages = get_career_averages(referee, career_totals)

    context = {
        'referee': referee,
        'matches': match_list,
        'first_match': matches.first(),
        'last_match': matches.last(),
        'career_totals': career_totals,
        'career_averages': career_averages,
        'nbar': 'referees'
    }
    return render(request, 'referee_bio.html', context)
