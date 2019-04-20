from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'hello/index.html')

def kasu(request):
    return render(request, 'hello/kasu.html')

def kariru(request):
    return render(request, 'hello/kariru.html')
