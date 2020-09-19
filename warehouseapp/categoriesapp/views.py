from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from infoserviceapp.models import InformationService
import datetime
import time

# Create your views here.

def index(request):
    return redirect('/productsapp/')
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    app = InformationService()
    now = app.mytime()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    return render(
        request, 'categories.html', context={'pname': pname, 'ip': ip,
        'info': info, 'year': now.year},
    )
