from django.urls import *

from referee.views import referee, referees

urlpatterns = [
    path('referees', referees, name='referees'),
    path('referees/<str:referee_id>/', referee)
]