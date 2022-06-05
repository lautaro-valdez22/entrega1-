from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from product.models import Celulares, Heladeras, Televisores
from product.forms import Celulares_form, Heladeras_form, Televisores_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Celulares.objects.all()
    context = {'celulares':Celulares}
    return render(request, 'celulares.html', context=context)

def products(request):
    print(request.method)
    productos = Heladeras.objects.all()
    context = {'heladeras': Heladeras}
    return render(request, 'heladeras.html', context=context)