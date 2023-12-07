from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import player_info , icc_batting,icc_bowling,icc_all_rounder
from rest_framework import viewsets
from .serializer import player_info_serializer,icc_all_rounder_serializer,icc_batting_serializer,icc_bowling_serializer


class player_info_viewset(viewsets.ModelViewSet):
    queryset = player_info.objects.all()
    serializer_class = player_info_serializer 
    search_fields=['name','country','gender']
    http_method_names = ['get', 'head', 'options']

class icc_batting_viewset(viewsets.ModelViewSet):
    queryset = icc_batting.objects.all()
    serializer_class = icc_batting_serializer
    search_fields=['position','rating','series']
    http_method_names = ['get', 'head', 'options']

class icc_bowling_viewset(viewsets.ModelViewSet):
    queryset = icc_bowling.objects.all()
    serializer_class = icc_bowling_serializer
    search_fields=['position','rating','series']
    http_method_names = ['get', 'head', 'options']

class icc_all_rounder_viewset(viewsets.ModelViewSet):
    queryset = icc_all_rounder.objects.all()
    serializer_class = icc_all_rounder_serializer
    search_fields=['position','rating','series']
    http_method_names = ['get', 'head', 'options']
    
    