from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    try:
        request.session['gold'] = 0
        request.session['activities']
    except:
        request.session['gold'] = request.session['gold']
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.POST['building'] == 'farm':
        earned = random.randrange(10, 21)
        request.session['gold'] += earned
        request.session['activities'].append('Earned ' + str(earned) + ' gold from the farm! ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif request.POST['building'] == 'cave':
        earned = random.randrange(5,11)
        request.session['gold'] += earned
        request.session['activities'].append('Earned ' + str(earned) + ' gold from the cave! ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif request.POST['building'] == 'house':
        earned = random.randrange(2,6)
        request.session['gold'] += earned
        request.session['activities'].append('Earned ' + str(earned) + ' gold from the farm! ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif request.POST['building'] == 'casino':
        earned = random.randrange(-50, 51)
        request.session['gold'] += earned
        if earned > 0:
            request.session['activities'].append('Entered a casino and won ' + str(earned) + ' gold! ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
        if earned < 0:
            request.session['activities'].append('Entered a casino and lost ' + str(earned) + ' gold... ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
        if earned == 0:
            request.session['activities'].append('Entered a casino and did not win or lose anything ' + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    print request.session['gold']
    return redirect('/')
