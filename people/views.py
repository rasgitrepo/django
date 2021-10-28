from django.shortcuts import render
from .models import People, Family, LinkFamilyMember

# Create your views here.
def home(request) :
    return render(request, 'inventory/home.html')

def member_list(request, Family):
    members = Family.objects.all()
    members.filter(id=Family.id) 
    return render(request, 'List') 
