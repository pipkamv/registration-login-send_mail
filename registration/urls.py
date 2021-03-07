from django.urls import path
from .views import *

app_name ='/'

urlpatterns = [
    path('', register, name='register'),
    path('edit/', edit, name='edit'),
]

