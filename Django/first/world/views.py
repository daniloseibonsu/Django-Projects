from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request, "world/index.html")
    
def see(request) :
    return HttpResponse('fuck me')

def much(request) :
    return HttpResponse('check this out')

def all(request, name) :
    return render(request, 'world/all.html',{
        'name': name.capitalize()
    } )
    