from django.shortcuts import render, HttpResponse, redirect
from .models import User
from time import gmtime, strftime

def index(request):
    data = {
        'all_users': User.objects.all()
    }
    return render(request, 'semi_restful/index.html', data)

def new(request):

    return render(request, 'semi_restful/new.html')
def create(request):
    if request.method == 'POST':
        q = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], created_at=strftime("%Y-%m-%d %H:%M %p", gmtime()))
        userId = q.id
        return redirect('/users/' + str(userId))
    else:
        return redirect('/users')
def show(request, user_id):
    if request.method =='GET':
        data = {
            'all_users': User.objects.all(),
            'first_name': User.objects.get(id=user_id).first_name,
            'last_name': User.objects.get(id=user_id).last_name,
            'email': User.objects.get(id=user_id).email,
            'created_at': User.objects.get(id=user_id).created_at,
            'id': User.objects.get(id=user_id).id,
        }
        return render(request, 'semi_restful/show.html', data)

def edit(request, user_id):
    if request.method == 'POST':
        data = {
            'all_users': User.objects.all(),
            'first_name': User.objects.get(id=user_id).first_name,
            'last_name': User.objects.get(id=user_id).last_name,
            'email': User.objects.get(id=user_id).email,
            'created_at': User.objects.get(id=user_id).created_at,
            'id': User.objects.get(id=user_id).id,
        }
        return render(request, 'semi_restful/edit.html', data)
    return redirect('/users')

def update(request, user_id):
    u = User.objects.get(id=user_id)
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.save()
    return redirect('/users')

def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/users')
