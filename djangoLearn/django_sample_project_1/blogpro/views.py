from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# take in request arguement

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
