from django.shortcuts import render

from django.http import HttpResponse
from .forms import homeForm


def index(request):
    return render(request, 'home/index.html')


def kasu(request):
    params = {
        'title': 'home',
        'message': 'your data:',
        'form': homeForm()
    }

    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = homeForm(request.POST)
    return render(request, 'home/kasu.html', params)


def kariru(request):
    return render(request, 'home/kariru.html')


def kakunin(request):
    name = request.POST['name']
    mail = request.POST['mail']
    age = request.POST['age']
    address = request.POST['address']
    money = request.POST['money']
    monkey = request.POST['monkey']
    params = {
        'name': name,
        'mail': mail,
        'age': age,
        'address': address,
        'money': money,
        'monkey': monkey,
    }
    return render(request, 'home/kakunin.html', params)
