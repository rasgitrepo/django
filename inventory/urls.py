from django.conf.urls import url
from .import views 

urlpatterns = [
 
    url('', views.home),
]   

#urlpatterns += staticfiles_urlpatterns()
