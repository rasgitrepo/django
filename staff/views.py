from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.
# @login_required
# def profile(request):
#     return render(request, 'staff/profile.html')

# def about(request):
#     return render(request,'staff/about.html')

# def home(request) :
#     return render(request, 'staff/home.html')

def profile(request):
    context = {

    }
    return render(request, 'staff/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'staff/profile_update.html', context)