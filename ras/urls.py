from django.contrib import admin
from django.conf.urls import url, include
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
 
    url('home/', views.home),
    url('admin/', admin.site.urls),
    url('inventory/', include('inventory.urls')),
    url('about/', views.about),
    url('accounts/', include('allauth.urls')),
]   

#urlpatterns += staticfiles_urlpatterns()
