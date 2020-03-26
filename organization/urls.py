from django. urls import *

from organization.views import clubs, club_bio

urlpatterns = [
    path('clubs', clubs, name="clubs"),
    path('clubs/<str:club_id>/', club_bio, name="club_bio")
]