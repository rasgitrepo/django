from django.shortcuts import render
from .models import Computer
from django.http import HttpResponse

# Create your views here.
 
def home(request):
    return render(request,'inventory/home.html')
