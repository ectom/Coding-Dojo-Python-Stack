from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    try:
		request.session["data"]
    except:
		request.session["data"] = []
    return render(request, 'session_words/index.html')

def process(request):
    if 'bold' in request.POST:
        bolded = '900'
    else:
        bolded = 'normal'
    data = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'bold': bolded,
        'time': '- added on ' + strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    request.session["data"].append(data)
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
