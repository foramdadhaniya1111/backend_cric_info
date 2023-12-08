from django.contrib import admin
from django.urls import path,include
from app import urls
from accounts import urls
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('accounts/',include('accounts.urls')),

    
]
