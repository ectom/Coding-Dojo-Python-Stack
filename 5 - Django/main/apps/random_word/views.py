from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'random_word/index.html')

def word(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    the_word = get_random_string(length=14)
    words = {
        'word': the_word
    }
    return render(request, 'random_word/index.html', words)
