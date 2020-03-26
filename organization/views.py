from django.shortcuts import render

from organization.models import Club

def clubs(request):
    clubs = Club.objects.all()
    context = {'nbar': 'clubs', 'clubs': clubs}
    return render(request, 'clubs.html', context)

def club_bio(request, club_id):
    pass
