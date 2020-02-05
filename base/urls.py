from django.conf.urls import *
from base.views import index

from config.urls import urlpatterns as config_url_patterns

urlpatterns = [
    url('', index)
]

urlpatterns += config_url_patterns