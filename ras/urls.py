from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from staff import views as user_views

urlpatterns = [
  
    url('admin/', admin.site.urls),
    url('home/', user_views.home, name='home'),
    url('about/', user_views.about, name='about'),
    url('accounts/', include('allauth.urls')),
    url('profile/', user_views.profile, name='profile'),
    url('login/', auth_views.LoginView.as_view(template_name='staff/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='staff/logout.html'), name='logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
