"""cricbuzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('player_info_api',views.player_info_viewset,basename='player_info'),
router.register('icc_batting',views.icc_batting_viewset,basename='icc_batting'),
router.register('icc_bowling',views.icc_bowling_viewset,basename='icc_bowling'),
router.register('icc_all_rounder',views.icc_all_rounder_viewset,basename='icc_all_rounder')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
