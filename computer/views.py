from django.shortcuts import render
from .models import Computer
from django.http import HttpResponse

# Create your views here.

def computer_detail(request, id=None, *args, **kwargs):
    print(args,kwargs)
    computer_obj = None
    if id is not None:
        computer_detail = Computer.objects.get(id=id)
    context = {
        "object": computer_obj,
    }
    return render(request, "computer_detail.html", context=context)

def computer_list(request):
    computers = Computer.objects.all().order_by('type','brand','model')
    return render(request,'computer/computer_list.html', {'computers': computers})
