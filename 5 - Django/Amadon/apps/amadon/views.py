from django.shortcuts import render, HttpResponse, redirect

def index(request):
    try:
        request.session['data']
        request.session['total_price'] = 0
        request.session['total_quantity'] = 0
    except:
        request.session['data'] = []
    return render(request, 'amadon/index.html')

def process(request):
    items = {
        '001': 19.99,
        '002': 29.99,
        '003': 4.99,
        '004': 49.99
    }
    data = {
        'quantity': int(request.POST['quantity'])
    }
    number = request.POST["product"]
    print items[number]
    request.session['data'].append(data)
    for item in request.session['data']:
        request.session['price'] = items[number]*item['quantity']
        request.session['total_price'] += (items[number]*item['quantity'])
        request.session['total_quantity'] += item['quantity']
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def clear(request):
    request.session.clear()
    return redirect('/')
