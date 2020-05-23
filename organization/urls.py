from django. urls import *
from rest_framework import routers

from organization.views import *

router = routers.DefaultRouter()
router.register(r'clubs', ClubsViewSet, basename="clubs")
router.register(r'clubs/<str:id>/', ClubsViewSet, basename="club_detail")

urlpatterns = [
    path('', include(router.urls))
]