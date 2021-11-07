from django.shortcuts import render

def about(request):
    return render(request,'staff/about.html')

def home(request) :
    return render(request, 'staff/home.html')



