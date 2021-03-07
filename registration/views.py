from django.shortcuts import render
from .forms import *
from .models import *


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            # profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/registration_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save(Profile)

    else:
        profile_form = ProfileEditForm()
        return render(request, 'registration/edit.html', {'profile_form': profile_form})
