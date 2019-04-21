from django.shortcuts import render

from django.http import HttpResponse
from .forms import HelloForm


def index(request):
    return render(request, 'hello/index.html')

def kasu(request):
    params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm()
        }
    
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/kasu.html', params)

def kariru(request):
    return render(request, 'hello/kariru.html')

def kakunin(request):
    name = request.POST['name']
    mail = request.POST['mail']
    age = request.POST['age']
    address = request.POST['address']
    money = request.POST['money']
    monkey = request.POST['monkey']
    params = {
        'name':name,
        'mail':mail,
        'age':age,
        'address':address,
        'money':money,
        'monkey':monkey,
    }
    return render(request, 'hello/kakunin.html', params)
