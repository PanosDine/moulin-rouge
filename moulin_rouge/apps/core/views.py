from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def products(request: HttpRequest) -> HttpResponse:
    return render(request, 'products.html')

def store(request: HttpRequest) -> HttpResponse:
    return render(request, 'store.html')

