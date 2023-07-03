from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from forms import MyForm

# Create your views here.
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'mytemp.html', {'form': form})
