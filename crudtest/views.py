from django.shortcuts import render

from django.http import HttpResponse
from crudtest.models import Friend


def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'all friends.',
        'data': data,
    }
    return render(request, 'crudtest/index.html', params)
