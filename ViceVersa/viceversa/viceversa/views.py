from django.http import HttpResponse
from django.shortcuts import render
import math

def about(request):
    return HttpResponse('<h1 style = "color: #ff0000">This is about page<h1>')

def home(request):
    a = math.sqrt(2**50)
    return render(request, 'home.html', {'greeting': 'Hello',
                                         'about' : 'This is about',
                                         'Wow': 'Look!',
                                         'lol': a})