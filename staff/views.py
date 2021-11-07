from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required
def profile(request):
    return render(request, 'staff/profile.html')

def about(request):
    return render(request,'staff/about.html')

def home(request) :
    return render(request, 'staff/home.html')
