from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
# Create your views here.

def index(request):
    return HttpResponse('work already')

def Enter_Question(request):
    if request.method == 'POST':
        form = Enter_Question(request.POST)
        if form.is_valid()