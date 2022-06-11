from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView   
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def menupage(request):
    return render(request, 'menupage.html')


def tableselect(request):
    return render(request, 'tableselect.html')

def qrcode(request):
    return render(request, 'qrcode.html')

def pay(request):
    return render(request, 'pay.html')


def sucess(request):
    return render(request, 'sucess.html')

    
     