from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'login_reg/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/log_reg')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user.count() > 0:
            messages.error(request, "email already taken", extra_tags="email")
            return redirect('/log_reg')
        else:
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            create_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
            request.session['user_id'] = create_user.id
            request.session['first_name'] = create_user.first_name
            request.session['last_name'] = create_user.last_name
            print user
            return redirect('/log_reg/success')
        return redirect('/log_reg/success')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users.count() > 0:
        user = users.first()
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()) == True:
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            print user
            return redirect('/log_reg/success')
        else:
            messages.error(request, "Login Failed", extra_tags="email")
            return redirect('/log_reg')
    else:
		messages.error(request, "Login Failed", extra_tags="email")
		return redirect('/log_reg')
def success(request):
    return render(request, 'login_reg/success.html')
