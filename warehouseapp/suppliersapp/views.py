from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from infoserviceapp.models import InformationService
from productsapp.models import Suppliers
import datetime
import time
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne
import pprint
import json

client = MongoClient()
db = client.nwwarehousedb

def index(request):
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    return render(
        request, 'suppliers.html', context={'pname': pname, 'ip': ip,
        'info': info, 'year': now.year},
    )

def suppliers(request):
    msg = "Enter New Suppliers Info: "
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    try:
        msg += " %s"%(now)
        print("@suppliers: %s"%(now))
        app = Suppliers()
        if request.method == 'POST':
            req = request.POST
            app.supplierID = req['supplierID'].strip()
            app.companyName = req['companyName'].strip()
            app.contactName = req['contactName'].strip()
            app.contactTitle = req['contactTitle'].strip()
            app.address = req['address'].strip()
            app.city = req['city'].strip()
            app.region = req['region'].strip()
            app.postalCode = req['postalCode'].strip()
            app.country = req['country'].strip()
            app.phone = req['phone'].strip()
            app.fax = req['fax'].strip()
            app.homePage = req['homePage'].strip()
            try:
                pdate = mytime2()
                print("Saving: %s, %s"%(app, pdate))
                checks = checkSupplierID(app)
                if( checks["supplierID"] == "None" ):
                    app.save()
                else:
                    return render(
                        request, 'supplierfeedback.html', context={
                        'time': pdate, 'message': "Already online, add another one.",
                        'app': app, 'year': pdate.year})
                message = "Done..Enjoy new WMS supplier."
                return render(
                    request, 'supplierfeedback.html', context={
                    'time': pdate, 'message': message,
                    'app': app, 'year': pdate.year})
            except Exception as e:
                msg += ", Error1: %s"%(e)
                print("Supplier Save1: %s"%(e))
    except Exception as e:
        msg += ", Error2: %s"%(e)
        print("Save supplier: %s"%(e))
    return render(
        request, 'suppliers.html', context={'pname': pname, 'ip': ip,
        'message': msg, 'info': info, 'year': now.year},
    )

def checksuppliers(request):
    db5 = []
    try:
        x = 0
        list = db.list_collection_names()
        dblist = "%s, %s"%(mytime2(), list)
        pprint.pprint(dblist)
        app = Suppliers()
        if request.method == 'GET':
            req = request.GET
            app.supplierID = req['pid'].strip()
            db3 = db.productsapp_suppliers.find_one({ "supplierID": app.supplierID })
            db5.append(db3)
            db5[x]['_id'] = "%s"%(db5[x]['_id'])
            pprint.pprint(db5)
            return HttpResponse(json.dumps(db5))
    except Exception as e:
        print("#@checksuppliers: %s %s"%(mytime2(), e))
    return HttpResponse(db5)

def checkSupplierID(app):
    try:
        db3 = db.productsapp_suppliers.find_one({ "supplierID": app.supplierID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.supplierID))
        return { "supplierID": db3["supplierID"] }
    except Exception as e:
        print("checkSupplierID: %s %s"%(mytime2(), e))
    return { "supplierID": "None" }

def wsuppliers(request):
    try:
        db3 = []
        db4 = db.productsapp_suppliers.find()
        x = 0
        for suppliers in db4:
            db3.append(suppliers)
            #db3[x]['_id'] = x+1
            db3[x]['_id'] = "%s"%(db3[x]['_id'])
            #print(db3[x]['_id'])
            x += 1
        db5 = json.dumps(db3)
        return HttpResponse(db5)
    except Exception as e:
        print("wsuppliers: %s"%(e))
    return HttpResponse(json.dumps([{ "info": "0" }]))

def suppliersReset():
    try:
        #db3 = db.productsapp_suppliers.bulk_write([ DeleteMany({}) ])
        #print(db3.bulk_api_result)
        return 1
    except Exception as e:
        raise
        print("suppliersReset %s %s")%(mytime2(), e)
    return -1

def dbreset(xyclient):
    try:
        xyclient.close()
    except Exception as e:
        print("#@dbreset: %s %s"%(mytime2(), e))
    return xyclient

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
