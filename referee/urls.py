from django.urls import *

from referee.views import referee_bio, referees

urlpatterns = [
    path('referees', referees, name='referees'),
    path('referees/<str:referee_id>/', referee_bio, name="referee_bio")
]