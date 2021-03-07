from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import Category, Product


def HomeView(request):
    return render(request, 'index.html')

def Productr(request):
    return render(request, 'product/product.html')

def contactform(reguest):
    if reguest.method =='POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['kanapmbm@gmail.com']


            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'kanapmbm@mgmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Допущен недопустимый заголовок')

            return HttpResponseRedirect('/shop/thanks/')

    else:
        form = ContactForm()
    return render(reguest, 'registration/contact.html', {'form':form, 'username':auth.get_user(reguest).username})



def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'registration/thanks.html', {'thanks':thanks})
