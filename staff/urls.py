from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from staff import views as user_views

urlpatterns = [
   
    path('profile', user_views.profile, name='profile'),
]   
