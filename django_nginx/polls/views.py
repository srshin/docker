from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def index(request):
    context = {'text': 'Hello, world. '}
    return render(request, 'polls/index.html', context)
