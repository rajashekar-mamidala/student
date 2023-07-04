from django import urls, forms, views
from django.urls import path

from .views import my_form
#from django import forms

app_name = 'student'

urlpatterns = [
    path('', my_form, name='my_form'),
]