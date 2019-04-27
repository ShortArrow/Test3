from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import homeForm
from .models import homeModel


def index(request):
    return render(request, 'home/index.html')


def kasu(request):
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


def kariru(request):
    data = homeModel.objects.all()  # レコードを表示する
    # form.save(commit=True)
    params = {
        'data': data,
        'form': homeForm()
    }
    return render(request, 'home/kariru.html', params)


def mailpage(request):
    return render(request, 'home/mailpage.html')
