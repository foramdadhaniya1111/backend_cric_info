from rest_framework import serializers
from .models import espncrici_player_info
from .models import player_info,icc_batting,icc_bowling,icc_all_rounder
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class player_info_serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = player_info
        fields = ['id','image','name','country','gender']
    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image)
        
class icc_batting_serializer(serializers.ModelSerializer):
    class Meta:
        
        model = icc_batting
        fields = '__all__'
        
class icc_bowling_serializer(serializers.ModelSerializer):
    class Meta:
        model = icc_bowling
        fields = '__all__'
        
class icc_all_rounder_serializer(serializers.ModelSerializer):
    class Meta:
        model = icc_all_rounder
        fields = '__all__'



class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = espncrici_player_info
        fields ="__all__"
    




