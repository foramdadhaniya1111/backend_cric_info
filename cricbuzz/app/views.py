
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import player_info , icc_batting,icc_bowling,icc_all_rounder,espncrici_player_info
from rest_framework import viewsets
from django.db.models import Q
from .serializer import player_info_serializer,icc_all_rounder_serializer,icc_batting_serializer,icc_bowling_serializer
from .models import espncrici_player_info
from .serializer import PlayerSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from .serializer import player_info_serializer,icc_all_rounder_serializer,icc_batting_serializer,icc_bowling_serializer,PlayerSerializer


class player_info_viewset(viewsets.ModelViewSet):
    queryset = player_info.objects.all()
    serializer_class = player_info_serializer 
    search_fields=['name','country','gender']
    http_method_names = ['get', 'head', 'options']

class icc_batting_viewset(viewsets.ModelViewSet):
    queryset = icc_batting.objects.all()
    serializer_class = icc_batting_serializer
    search_fields = ['position', 'rating', 'series']
    http_method_names = ['get', 'head', 'options']

    def list(self, request):
        queryset = self.get_queryset().select_related('player')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class icc_bowling_viewset(viewsets.ModelViewSet):
    queryset = icc_bowling.objects.all()
    serializer_class = icc_bowling_serializer
    search_fields=['position','rating','series']
    http_method_names = ['get', 'head', 'options']

    def list(self, request):
        queryset = self.get_queryset().select_related('player')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class icc_all_rounder_viewset(viewsets.ModelViewSet):
    queryset = icc_all_rounder.objects.all()
    serializer_class = icc_all_rounder_serializer
    search_fields=['position','rating','series']
    http_method_names = ['get', 'head', 'options']



class playerViewSet(viewsets.ModelViewSet):
    queryset = espncrici_player_info.objects.all()
    serializer_class = PlayerSerializer
    filterset_fields =['player_country','player_gender','player_playing_role']

# class afghanistan_player(viewsets.ModelViewSet):
#     queryset = espncrici_player_info.objects.filter(player_country='afghanistan-40').
#     serializer_class = PlayerSerializer

class filtration_player(viewsets.ModelViewSet):
    queryset = espncrici_player_info.objects.all()
    serializer_class = PlayerSerializer
    # filter_backends =[SearchFilter]
    # search_fields = ['player_country','player_gender','player_playing_role']
    # http_method_names = ['get', 'head', 'options','post']
    def get_queryset(self):
        player_country = self.request.GET.get('player_country')
        player_gender = self.request.GET.get('player_gender')
        player_playing_role = self.request.GET.get('player_playing_role')
        if player_country and player_gender and player_playing_role:
            qs = espncrici_player_info.objects.filter(Q(player_country=player_country) & Q(player_gender=player_gender)  & Q(player_playing_role=player_playing_role))
        elif player_country and player_gender:
            qs = espncrici_player_info.objects.filter(Q(player_country=player_country) & Q(player_gender=player_gender))
        elif player_country and player_playing_role:
            qs = espncrici_player_info.objects.filter(Q(player_country=player_country) & Q(player_playing_role=player_playing_role))
        elif player_gender and player_playing_role:
             qs = espncrici_player_info.objects.filter(Q(player_gender=player_gender)  & Q(player_playing_role=player_playing_role))
        elif player_country:
            qs = espncrici_player_info.objects.filter(Q(player_country=player_country))
        elif player_gender:
            qs = espncrici_player_info.objects.filter(Q(player_gender=player_gender))
        elif player_playing_role:
            qs = espncrici_player_info.objects.filter(Q(player_playing_role=player_playing_role))

        return qs
