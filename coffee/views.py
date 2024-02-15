from django.shortcuts import render
from django.http import HttpResponse
from  .models import coffee
from django.template import loader

# Create your views here.

def home(request):
    coffee = coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})