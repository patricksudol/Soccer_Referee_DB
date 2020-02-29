from django.urls import *
from base.views import index

from config.urls import urlpatterns as config_urlpatterns
from referee.urls import urlpatterns as referee_urlpatterns
from organization.urls import urlpatterns as organization_urlpatterns

# TODO: Abstract urls
urlpatterns = [
    path('', index)
]

urlpatterns += config_urlpatterns
urlpatterns += referee_urlpatterns
urlpatterns += organization_urlpatterns
