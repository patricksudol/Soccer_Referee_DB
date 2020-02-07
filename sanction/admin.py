from django.contrib import admin

from sanction.models.card import YellowCard, RedCard
from sanction.models.penalty import Penalty

admin.site.register(YellowCard)
admin.site.register(RedCard)
admin.site.register(Penalty)

