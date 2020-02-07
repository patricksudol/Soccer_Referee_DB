from django.contrib import admin

from organization.models.club import Club
from organization.models.match import Match
from organization.models.season import Season

admin.site.register(Club)
admin.site.register(Match)
admin.site.register(Season)
