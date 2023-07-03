from django import urls, views, forms
from django.urls import path
#from .views import student
#from django import forms

app_name = 'student'

urlpatterns = [
    #path('', student, name='Myform'),
    urls(r'form', views.my_form, name='form')
]