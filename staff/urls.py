from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from staff import views as user_views

urlpatterns = [
   
    path('profile', user_views.profile, name='profile'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
