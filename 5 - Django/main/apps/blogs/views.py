from django.shortcuts import render, HttpResponse, redirect

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
def show(request, number):
    response = 'Placeholder to display blog ' + number
    return HttpResponse(response)
def edit(request, number):
    response = 'Placeholder to edit blog ' + number
    return HttpResponse(response)
def destroy(request, number):
    print 'destroy'
    return redirect('/blogs')
