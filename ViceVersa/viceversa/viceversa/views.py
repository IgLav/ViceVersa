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

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text= user_text[::-1]
    words_count = len(user_text.split())
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext': reversed_text,
                                            'wordscount': words_count})