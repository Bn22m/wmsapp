from django.shortcuts import render, redirect
from django.http import HttpResponse
from infoserviceapp.models import InformationService
import json


def index(request):
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    app = InformationService()
    now = app.mytime()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    db5 = json.dumps(info)
    return HttpResponse(db5)
