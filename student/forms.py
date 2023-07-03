from django import forms
from .models import Member

class MyForm(forms.ModelForm):
  class Meta:
    model = Member
    fields = ["fullname", "mobile_number",]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number",}