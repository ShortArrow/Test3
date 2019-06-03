from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import homeForm
from .forms import kensakuForm
from .models import homeModel
from django.core.paginator import Paginator
from .forms import MessageForm
from .models import Message


def index(request):
    params = {
        'title': "SPACE BOOKING",
        'message': "貸したい人と借りたい人をマッチングするサービスです。",
    }
    return render(request, 'home/index.html', params)


def kasu(request):   #本の中のcreate関数
    params = {
        'form': homeForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        age = request.POST['age'] 
        address = request.POST['address']
        money = request.POST['money']
        homeSaver = homeModel(name=name, mail=mail,
                              age=age, address=address, money=money)
        homeSaver.save()
        return redirect(to='/kariru')
    return render(request, 'home/kasu.html', params)


def kakunin(request):
    name = request.POST['name']
    mail = request.POST['mail']
    age = request.POST['age']
    address = request.POST['address']
    money = request.POST['money']
    params = {
        'name': name,
        'mail': mail,
        'age': age,
        'address': address,
        'money': money,
    }
    return render(request, 'home/kakunin.html')


def kariru(request, num=1):
    data = homeModel.objects.all()  # レコードを表示する
    # form.save(commit=True)
    page = Paginator(data, 3)
    params = {
        'data': page.get_page(num),
        'form': homeForm(),
        'form2': kensakuForm(),
    }
    if (request.method == 'POST'):   #検索された時の処理
        num = request.POST['address']
        item = homeModel.objects.get(address=num)
        params['data'] = [item]
        params['form'] = kensakuForm(request.POST)

    return render(request, 'home/kariru.html', params)


def mailpage(request):
    return render(request, 'home/mailpage.html')

def edit(request, num):
    obj = homeModel.objects.get(id=num)
    if (request.method == 'POST'):   #更新ではなく、追加になってしまう
        space = homeForm(request.POST, instance=obj)
        space.save()
        return redirect(to='/kariru')
    params = {
        'id': num,
        'form': homeForm(instance=obj),
    }
    return render(request, 'home/edit.html', params)

def delete(request, num):
    space = homeModel.objects.get(id=num)
    if (request.method == 'POST'):
        space.delete()
        return redirect(to=kariru)
    params = {
        'id':num,
        'obj': space
    }
    return render(request, 'home/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        form =  kensakuForm(request.POST)
        str = request.POST['find']
        data = homeModel.objects.filter(address__contains=str)
    else:
        form =  kensakuForm()
        data = homeModel.objects.all()
    params = {
        'form':form,
        'data':data,
    }
    return render(request, 'home/find.html', params)

def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'form': MessageForm(),
        'data': paginator.get_page(page)
    }
    return render(request, 'home/message.html', params)