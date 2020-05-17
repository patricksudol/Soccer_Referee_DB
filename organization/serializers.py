from organization.models import Club

from rest_framework import serializers


class ClubsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'club_id', 'name', 'is_active']