from django. urls import *
from rest_framework import routers
# from organization.views import clubs, club_bio
from organization.views import *

router = routers.DefaultRouter()
router.register(r'clubs', ClubsViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('clubs', clubs, name="clubs"),
    # path('clubs/<str:club_id>/', club_bio, name="club_bio")
]