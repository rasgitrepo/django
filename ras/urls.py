from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
 
    url('home/', views.home),
    url('admin/', admin.site.urls),
    url('inventory/', include('inventory.urls')),
    url('about/', views.about),
    url('accounts/', include('allauth.urls')),
   # url('login/', auth_views_LoginView.as_view(template_name='user/login.html'), name='user-login'),
    #url('logout/', auth_views_LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
]   

#urlpatterns += staticfiles_urlpatterns()
