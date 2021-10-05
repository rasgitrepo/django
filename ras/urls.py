from django.contrib import admin
from django.conf.urls import url, include
from .views import home, about
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
 
    url('admin/', admin.site.urls),
    url('computer/', include('computer.urls')),
    url('about/', about),
    url('', home),
]   

#urlpatterns += staticfiles_urlpatterns()
