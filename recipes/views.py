from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Page: Home')    

def about(request):
    return HttpResponse('Page: Sobre')

def contacts(request):
    return HttpResponse('Page: Contatos')    

