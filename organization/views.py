from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from referee.models import Referee
from organization.models import Club, Match
from organization.serializers import ClubsSerializer

# def clubs(request):
#     clubs_query = Club.objects.all()
#     clubs = []
#     for counter, club in enumerate(clubs_query, start=1):
#         club = {
#             'club_obj': clubl,
#             'first_in_row': True if counter % 4 == 1 else False
#         }
#         clubs.append(club)
#     context = {'nbar': 'clubs', 'clubs': clubs}
#     return render(request, 'clubs.html', context)

# def club_bio(request, club_id):
#     club = Club.objects.get(club_id=club_id)
#     referees = Referee.objects.filter(id__in=club.all_matches.values_list(
#         'referee',
#         flat=True
#     ))
#     ref_objs = []
#     for referee in referees:
#         ref_obj = {
#             'referee': referee,
#             'matches': Match.objects.filter(referee=referee)
#         }
#         ref_objs.append(ref_obj)
    
    # context = {'nbar': 'clubs', 'club': club, 'ref_objs': ref_objs}
    # return render(request, 'club.html', context)


class ClubsViewSet(viewsets.ViewSet):

    queryset = Club.objects.all()

    def list(self, request):
        queryset = Club.objects.all()
        serializer = ClubsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Club.objects.all()
        club = get_object_or_404(queryset, pk=pk)
        serializer = ClubsSerializer(club)
        return Response(serializer.data)
