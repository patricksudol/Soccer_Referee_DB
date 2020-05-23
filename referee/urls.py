from django.urls import *
from rest_framework import routers

from referee.views import RefereeViewSet

router = routers.DefaultRouter()
router.register(r'referees', RefereeViewSet, basename='referees')
router.register(r'referees/<str:id>/', RefereeViewSet, basename='referee_detail')

urlpatterns = [
    path('', include(router.urls))
]
