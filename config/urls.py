from django.contrib import admin
from django.urls import path

# TODO: Consider Include()
urlpatterns = [
    path('admin/', admin.site.urls),
]
