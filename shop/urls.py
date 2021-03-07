from django.urls import path
from .views import *
app_name = 'shop'

urlpatterns = [
    path('home/', HomeView, name='home'),
    path('product/', Product, name='product'),
    path('contact/', contactform, name='contact'),
    path('thanks/', thanks, name='thanks'),
]




