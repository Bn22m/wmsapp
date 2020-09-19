from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne
import pprint
import json
from datetime import datetime, timedelta
import datetime
import time
from dateutil.parser import parse
import os
import os.path
from infoserviceapp.models import InformationService
from productsapp.models import Suppliers, Products, OrderDetails
from categoriesapp.models import UploadCategory
from bson.json_util import loads

client = MongoClient()
db = client.nwwarehousedb


def index(request):
    txtmore = 50
    txtfilterid = ''
    now = mytime2()
    db3 = []
    dbl = '0'
    print("productsapp index: %s"%(now))
    try:
        db3 = info12()
        dbl = db.productsapp_products.count_documents({})
        txtfilterid = request.session['txtfilterid']
        txtmore = request.session['txtmore']
    except Exception as e:
        print("More:  %s %s %s %s"%(now , dbl , txtmore, e))
        request.session['txtmore'] = 100
        request.session['txtfilterid'] = ''
        txmore = 50
        txtfilterid = ''
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    app = InformationService()
    service = app.wsproducts()
    #paginator = Paginator(service, txtmore)
    #db33 = [db3, service]
    for x in service:
        db3.append(x)
    paginator = Paginator(db3, txtmore)
    page = request.GET.get('page')
    pproducts = paginator.get_page(page)
    #dbproducts = service
    #dblen = len(service)
    dbproduct = json.dumps(db3)
    #dbproduct = db3
    return render(
        request, 'products.html', context={'pname': pname, 'ip': ip,
        'info': info, 'dbl': dbl, 'dbproduct': dbproduct, 'txtmore': txtmore,
         'txtfilterid': txtfilterid, 'pproducts': pproducts, 'year': now.year},
    )

def newproduct(request):
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    return render(
        request, 'newproduct.html', context={'pname': pname, 'ip': ip,
        'info': info, 'year': now.year},
    )

def getproducts(request):
    try:
        if request.method == 'POST':
            qrb = request.POST
            more = qrb['txtmore'].strip()
            print("More: %s"%(more))
            pname = 'Northwind WMS'
            ip = request.META['REMOTE_ADDR']
            db3 = info12()
            dblen = db.productsapp_products.count_documents({})
            app = InformationService()
            now = app.mytime()
            info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
            service = app.wsproducts()
            for x in service:
                db3.append(x)
            paginator = Paginator(db3, more)
            page = request.GET.get('page')
            pproducts = paginator.get_page(page)
            #dbproducts = service
            #dblen = len(service)
            #dbproduct = json.dumps(dbproducts)
            dbproduct = json.dumps(db3)
            request.session['txtmore'] = more
            return render(
                request, 'products.html', context={'pname': pname, 'ip': ip,
                'dblen': dblen, 'pproducts': pproducts, 'info': info,
                'dbproduct': dbproduct, 'txtmore': txtmore, 'year': now.year},
            )
    except Exception as e:
        print("getproducts: %s %s"%(mytime2(), e))
    return redirect('/productsapp/')

def wproducts(request):
    try:
       db3 = []
       db4 = db.productsapp_products.find()
       x = 0
       for products in db4:
           db3.append(products)
           #db3[x]['_id'] = x+1
           db3[x]['_id'] = "%s"%(db3[x]['_id'])
           #print(db3[x]['_id'])
           x += 1
       db5 = json.dumps(db3)
       return HttpResponse(db5)
    except Exception as e:
        print("wproducts: %s"%(e))
    return HttpResponse(json.dumps([{ "SystemError": "0" }]))

def updateproducts(request):
    return redirect('/productsapp/newproduct')

def categories(request):
    try:
        if request.method == 'POST':
            req = request.POST
            filterid = req['categoryID'].strip()
            request.session['txtmore'] = 100
            request.session['txtfilterid'] = filterid
    except Exception as e:
        print("categories: %s"%(e))
    return redirect('/productsapp/')

def suppliers(request):
    return redirect('/suppliersapp/')

def newproducts(request):
    msg = "Enter New Product Info: "
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    try:
        msg += " %s"%(now)
        print("newproducts: %s"%(now))
        app = Products()
        if request.method == 'POST':
            req = request.POST
            app.productID = req['productID'].strip()
            app.productName = req['productName'].strip()
            app.supplierID = req['supplierID'].strip()
            pfile2 = fileupload(request, req['categoryID'].strip())
            print("cppicture: %s"%(pfile2))
            cpfile = urlpicture(pfile2[1].strip())
            app.categories = {
                "categoryID": req['categoryID'].strip(),
                "categoryName": req['categoryName'].strip(),
                "description": req['description'].strip(),
                "picture": cpfile
            }
            app.quantityPerUnit = req['quantityPerUnit'].strip()
            app.unitPrice = req['unitPrice'].strip()
            app.unitsInStock = req['unitsInStock'].strip()
            app.unitsOnOrder = req['unitsOnOrder'].strip()
            app.reorderLevel = req['reorderLevel'].strip()
            try:
                pdate = mytime2()
                print("Saving new product: %s %s"%(app, pdate))
                ckp = checkProductID(app)
                if( ckp["productID"] == "None" ):
                    app.save()
                else:
                    return render(
                        request, 'productfeedback.html', context={
                        'time': pdate, 'message': "This product is already online, add another one.",
                        'app': app, 'year': pdate.year})
                message = "Done..Enjoy new WMS product."
                print("cpfile: %s"%(cpfile))
                return render(
                    request, 'productfeedback.html', context={
                    'time': pdate, 'message': message,
                    'app': app, 'year': pdate.year})
            except Exception as e:
                msg += ", Error1: %s"%(e)
                print("Product Save1: %s"%(e))
    except Exception as e:
        msg += ", Error2: %s"%(e)
        print("Save product: %s"%(e))
    return render(
        request, 'newproduct.html', context={'pname': pname, 'ip': ip,
        'message': msg, 'info': info, 'year': now.year},
    )

def fileupload(request, categoryid):
    t2 = mytime2()
    if request.method == 'POST':
        req = request.POST
        req2 = request.FILES
        qrsize = req2['filename'].size
        maxb = (1024 * 500)
        if qrsize > maxb:
            return [0, qrsize]
        form = UploadCategory(req, req2)
        print("%sB/%sB"%(qrsize, maxb))
        if form.is_valid():
            #freq = req2['filename'].file.read()
            pfile, pext =  form.sanitizefile()
            if pext == 0:
                return [0, 0]
            freq = pfile.file.read()
            fle = saveFile(freq, categoryid, pext)
            fl3 = "file: %s-%s-%s"%(t2, fle, qrsize)
            print(fl3)
            if fle == 0:
                return [0, 0]
            return [1, fle]
        else:
            return [0, 0]
    else:
        return [0, 0]
    return [0, 0]

def saveFile(fle, categoryid, pext):
    jpg = 'categoriesapp/static/categoriesapp/cpicture/%s.%s'%(categoryid, pext)
    #jpg = 'categoriesapp/cpicture/%s.%s'%(categoryid, pext)
    print(jpg)
    try:
        path = default_storage.save(jpg, ContentFile(fle))
        return path
    except Exception as e:
        print("%s-%s"%(jpg, e))
        return 0
    return 0

def checkFile(fle):
    try:
        pro = os.path.isfile(fle)
        return pro
    except Exception as e:
        print("Fle: %s-%s-%s"%(mytime2(), fle, e))
    return False

def urlpicture(picture):
    try:
        urlp = picture.split('static/')
        return "%s"%(urlp[1])
    except Exception as e:
        raise
    return picture

def info11():
    db11 = []
    try:
        #client = MongoClient()
        #db = client.nwwarehousedb
        print("#01 %s %s"%(mytime2(), client))
        list = db.list_collection_names()
        dblist = "%s, %s"%(mytime2(), list)
        print(dblist)
        #db3 = db.productsapp_products.find_one()
        #pprint.pprint(db3)
        db4 = db.productsapp_products.find()
        print("#db4: %s"%(mytime2()))
        pprint.pprint(db4[0])
        #print(db4)
        #for x in db4:
        #    pprint.pprint(x)
        #print("#000: %s %s %s %s %s %s"%(mytime2(), n, db3[0].productID, db3[0].productName, db3[0].unitPrice, db3[0].discontinued))
        return dblist
    except Exception as e:
        print("%s"%(e))
    return db11

def info12():
    db3 = []
    db4 = db.productsapp_products.find()
    x = 0
    for products in db4:
        db3.append(products)
        #db3[x]['_id'] = x+1
        db3[x]['_id'] = "%s"%(db3[x]['_id'])
        #print(db3[x]['_id'])
        x += 1
    #db5 = json.dumps(db3)
    return db3

def checkcategories(request):
    try:
        db5 = []
        x = 0
        app = Products()
        if request.method == 'GET':
            req = request.GET
            app.productID = req['pid'].strip()
            db3 = db.productsapp_products.find_one({ "productID": app.productID })
            db5.append(db3)
            db5[0]['_id'] = "%s"%(db5[0]['_id'])
            return HttpResponse(json.dumps(db5))
    except Exception as e:
        print("checkcategories: %s %s"%(mytime2(), e))
    return HttpResponse(json.dumps({ "categoryID": "None", "categoryName": "None", "description": "None" }))

def checkProductID(app):
    try:
        db3 = db.productsapp_products.find_one({ "productID": app.productID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.productID))
        return { "productID": db3["productID"] }
    except Exception as e:
        print("checkProductID: %s %s"%(mytime2(), e))
    return { "productID": "None" }

def productsReset():
    try:
        #print("#Don't try this at home kids!")
        #db3 = db.productsapp_products.bulk_write([ DeleteMany({}) ])
        #print("productsReset %s %s")%(mytime2(), db3.bulk_api_result)
        return 1
    except Exception as e:
        print("productsReset %s %s")%(mytime2(), e)
    return -1

def checkproducts(request):
    db5 = []
    try:
        x = 0
        print("@checkproducts: %s"%(mytime2()))
        if request.method == 'GET':
            app = Products()
            req = request.GET
            app.productID = req['pid'].strip()
            db3 = db.productsapp_products.find_one({ "productID": app.productID })
            db5.append(db3)
            db5[x]['_id'] = "%s"%(db5[x]['_id'])
            pprint.pprint(db5)
            return HttpResponse(json.dumps(db5))
    except Exception as e:
        print("#@checkproducts: %s %s"%(mytime2(), e))
    return HttpResponse(db5)

def updateorders(request):
    msg = "New Orders Info: "
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    print("@updateorders: %s"%(now))
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    db5 = []
    x = 0
    try:
        msg += " %s"%(now)
        app1 = OrderDetails()
        if request.method == 'GET':
            req = request.POST
            app1.productID = req['productID'].strip()
            app1.quantity = req['quantity'].strip()
            f = DecimalField(max_digits=9, decimal_places=2)
            app = Products()
            app.productID = app1.productID
            #app.unitsOnOrder
            db3 = db.productsapp_products.find_one({ "productID": app.productID })
            v1 = db3["unitsOnOrder"]
            unitsx = f.clean(v1) + f.clean(app1.quantity)
            print(unitsx)
            db3["unitsOnOrder"] = unitsx
            db4 = db.productsapp_products.find_one_and_update(db3)
            print("#updateProductsOrders %s: %s + %s = %s"%(mytime2(), v1, app1.quantity, unitsx))
            db5.append(db3)
            db5[x]['_id'] = "%s"%(db5[x]['_id'])
            pprint.pprint(db5)
            return HttpResponse(json.dumps(db5))
    except Exception as e:
            print("@updateProductsOrders: %s %s"%(mytime2(), e))
    return HttpResponse(db5)

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
