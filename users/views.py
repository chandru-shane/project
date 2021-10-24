from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from .models import Profile
from .forms import ProfileUpdateForm

# Create your views here.
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    # getting profile
    try:
        profile = Profile.objects.get(user=request.user)
    except exceptions.ObjectDoesNotExist:
        #create profile
        profile = Profile.objects.create(user=request.user)
    return render(request,'profile.html', {'profile':profile})

@login_required
def profile_update(request):
    
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            messages.success(request, f'Success fully updated')
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'form':profile_form})
