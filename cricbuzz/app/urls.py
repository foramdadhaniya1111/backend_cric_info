
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from . import views

router = DefaultRouter()
router.register('player_info_api',views.player_info_viewset,basename='player_info'),
router.register('icc_batting',views.icc_batting_viewset,basename='icc_batting'),
router.register('icc_bowling',views.icc_bowling_viewset,basename='icc_bowling'),
router.register('icc_all_rounder',views.icc_all_rounder_viewset,basename='icc_all_rounder'),
router.register('playerapi',views.playerViewSet , basename='allplayer'),
# router.register('afghanistan_player',views.afghanistan_player , basename='afghanistan-40'),
urlpatterns = [
    path('',include(router.urls)),
    
]
