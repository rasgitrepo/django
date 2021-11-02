from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    url('admin/', admin.site.urls),
    url('inventory/', include('inventory.urls')),
    url('accounts/', include('allauth.urls')),
    url('login/', auth_views.LoginView.as_view(template_name='staff/login.html'), name='user-login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='staff/logout.html'), name='user-logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
