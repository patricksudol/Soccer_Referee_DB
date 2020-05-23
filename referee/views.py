from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets

from referee.models import Referee
from referee.utils.career_totals import (
    get_career_averages,
    get_career_totals,
    referee_info,
    total_matches_by_position
)


def referees(request, page_number):
    referee_queryset = Referee.objects.all().order_by('name_family')
    referees_list = []
    paginator = Paginator(referee_queryset, 12)
    for counter, referee in enumerate(paginator.object_list, start=1):
        ref_dict = referee_info(referee)
        ref_dict.update(
            {
                'count': counter,
                'first_in_row': True if counter % 4 == 1 else False
            }
        )
        referees_list.append(ref_dict)
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

    career_totals = get_career_totals(referee)
    career_averages = get_career_averages(referee, career_totals)

    context = {
        'referee': referee,
        'matches': matches,
        'career_totals': career_totals,
        'career_averages': career_averages,
        'nbar': 'referees'
    }
    context.update(total_matches_by_position(referee, matches))
    return render(request, 'referee_bio.html', context)


class RefereeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Referee.objects.all()
        serializer = RefereeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Referee.objects.all()
        referee = get_object_or_404(queryset, pk=pk)
        serializer = RefereeSerializer(referee)
        return Response(serializer.data)
