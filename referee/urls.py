from django.urls import *

from referee.views import referees

urlpatterns= [
    path('referees', referees)
]