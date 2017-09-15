from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        request.session['data'] = {
            'the_name': request.POST['name'],
            'the_location': request.POST['location'],
            'the_language': request.POST['language'],
            'the_comment': request.POST['comment'],
        }
        print 'process'
        return redirect('/result')
    else:
        return redirect('/result')

def result(request):
    return render(request, 'survey/result.html')
