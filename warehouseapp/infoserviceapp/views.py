from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from infoserviceapp.models import InformationService

# Create your views here.

def index(request):
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    app = InformationService()
    now = app.mytime()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    return render(
        request, 'wms.html', context={'pname': pname, 'message': now,
        'info': info, 'year': now.year},
    )

def products(request):
    return redirect('/productsapp/')

def orders(request):
    return redirect('/ordersapp/')

def suppliers(request):
    return redirect('/suppliersapp/')

def categories(request):
    return redirect('/categoriesapp/')
