from .views import RegisteraAPI,LoginAPI
from django.urls import path
from knox import views as knox_views
from . import views
urlpatterns = [
    path('api/register/',RegisteraAPI.as_view(),name='register'),
    path('api/login/',LoginAPI.as_view(),name='login'),
    path('api/logout/',knox_views.LogoutView.as_view(),name='logout'),
    path('api/user/',views.userview.as_view(),name='user'),
    
]
