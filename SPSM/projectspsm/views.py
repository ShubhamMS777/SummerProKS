from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import ProductData


def index(request):
    return render(request, 'index.html')

def prod(request):
    prodet = ProductData.objects.all()
    return render(request, 'product2.html', {'prodet': prodet })

def test(request):
    return render(request, 'test1.html')