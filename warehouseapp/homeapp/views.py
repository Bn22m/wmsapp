from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from infoserviceapp.models import InformationService
import datetime
import time

# Create your views here.
def index(request):
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    app = InformationService()
    service = app.isminfo()
    paginator = Paginator(service, 3)
    page = request.GET.get('page')
    info = paginator.get_page(page)
    project = '/aboutapp/project2020.jpg'
    return render(
        request, 'index.html', context={'pname': pname, 'message': now,
        'project': project, 'info': info, 'ip': ip, 'year': year},
    )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    print("Home: %s-%s, %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
