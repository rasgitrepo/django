from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from staff import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('staff.urls')),
    path('', auth_views.LoginView.as_view(template_name='staff/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='staff/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('profile/update/', user_views.profile_update, name='user-profile-update'),
    path('logout/', auth_views.LogoutView.as_view(template_name='staff/logout.html'), name='logout'),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)