from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render

from .models import *

class UserRegistrationForm(forms.ModelForm):
    password  = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password(self):
        cd = self.cleaned_data
        if 'password' in cd and 'password2' in cd and cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают, попробуйте еще раз.')
        return cd


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)


