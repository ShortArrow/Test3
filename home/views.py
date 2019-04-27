from django.shortcuts import render

from django.http import HttpResponse
from .forms import homeForm
from .models import homeModel 


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


def kakunin(request):
    name = request.POST['name']
    mail = request.POST['mail']
    age = request.POST['age']
    address = request.POST['address']
    money = request.POST['money']
    params = {
        'name':name,
        'mail':mail,
        'age':age,
        'address':address,
        'money':money,
    }
    return render(request, 'home/kakunin.html')

def kariru(request):
    data = homeModel.objects.all() #レコードを表示する
    # form.save(commit=True)
    params = {
        'data': data,
        'form': homeForm()
    }
    return render(request, 'home/kariru.html', params)
