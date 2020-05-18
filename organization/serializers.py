from referee.models import Referee
from organization.models import Club, Match

from rest_framework import serializers


class RefereeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Referee
        fields = ['name_common', 'is_active']


class MatchSerializer(serializers.ModelSerializer):
    
    referee = RefereeSerializer()
    class Meta:
        model = Match
        fields = ['match_id', 'referee']


class ClubsSerializer(serializers.ModelSerializer):
    
    home_matches = MatchSerializer(many=True)
    
    class Meta:
        model = Club
        fields = ['name', 'club_id', 'is_active', 'home_matches']
