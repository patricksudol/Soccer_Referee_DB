from django. urls import *

from organization.views import *

urlpatterns = [
    path('clubs', clubs, name="clubs"),
    path('referees/<str:club_id>/', club_bio, name="club_bio")
]