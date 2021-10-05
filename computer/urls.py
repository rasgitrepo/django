from django.conf.urls import url
from .import views

urlpatterns = [
url('computer/<int:id>/', views.computer_detail),
url('', views.computer_list),

]
