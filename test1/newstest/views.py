from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.

def index(request):
    return HttpResponse("index")
    pass