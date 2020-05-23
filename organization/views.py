from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from organization.models import Club
from organization.serializers import ClubsSerializer

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
