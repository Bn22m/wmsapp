from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from django.forms import DecimalField, ValidationError, Widget
from infoserviceapp.models import InformationService
from productsapp.models import OrderDetails, Products
import datetime
import time
import pymongo
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
        request, 'orders.html', context={'pname': pname, 'ip': ip,
        'info': info, 'year': now.year},
    )

def orders(request):
    msg = "Enter New Orders Info: <br>"
    pname = 'Northwind WMS'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    info = [{'ip': ip}, {'time': str(now)}, {'is': pname}]
    try:
        msg += " %s"%(now)
        app = OrderDetails()
        if request.method == 'POST':
            req = request.POST
            app.orderID = req['orderID'].strip()
            app.productID = req['productID'].strip()
            app.unitPrice = req['unitPrice'].strip()
            app.quantity = req['quantity'].strip()
            app.discount = req['discount'].strip()
            try:
                app.unitPrice = float(app.unitPrice)
                app.quantity = float(app.quantity)
                app.discount = float(app.discount)
                pdate = mytime2()
                print("Saving Orders Details: %s %s"%(app, pdate))
                checks = checkOrderID(app)
                if( checks["orderID"] == "None" ):
                    app.save()
                    msg += "product saved %s"%(mytime2())+"<br>"
                    msg += " "+app.orderID+"<br>"
                    msg += "updating product orders...<br>"
                    dbr = updateorders2(app)
                else:
                    return render(
                        request, 'ordersfeedback.html', context={
                        'time': pdate, 'message': "Already online, add another one.",
                        'dorders': app, 'updates': checks, 'year': pdate.year})
                message = "Done..Enjoy new WMS order details."
                return render(
                    request, 'ordersfeedback.html', context={
                    'time': pdate, 'message': message,
                    'dorders': app, 'updates': dbr, 'year': pdate.year})
            except Exception as e:
                msg += ", Error1: %s"%(e)
                print("Orders Save1: %s"%(e))
    except Exception as e:
        msg += ", Error2: %s"%(e)
        print("Save orders: %s"%(e))
    return render(
        request, 'orders.html', context={'pname': pname, 'ip': ip,
        'message': msg, 'info': info, 'year': now.year},
    )

def checkOrderID(app):
    try:
        db3 = db.productsapp_orderdetails.find_one({ "orderID": app.orderID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.orderID))
        return { "orderID": db3["orderID"] }
    except Exception as e:
        print("checkOrderID: %s %s"%(mytime2(), e))
    return { "orderID": "None" }

def worders(request):
    try:
        db3 = []
        db4 = db.productsapp_orderdetails.find()
        x = 0
        for orders in db4:
            db3.append(orders)
            #db3[x]['_id'] = x+1
            db3[x]['_id'] = "%s"%(db3[x]['_id'])
            #print(db3[x]['_id'])
            x += 1
        db5 = json.dumps(db3)
        return HttpResponse(db5)
    except Exception as e:
        print("worders: %s"%(e))
    return HttpResponse(json.dumps([{}]))

def orderdetails(request):
    db5 = []
    try:
        x = 0
        app = OrderDetails()
        if request.method == 'GET':
            req = request.GET
            app.orderID = req['pid'].strip()
            db3 = db.productsapp_orderdetails.find_one({ "orderID": app.orderID })
            db5.append(db3)
            db5[x]['_id'] = "%s"%(db5[0]['_id'])
            pprint.pprint(db5)
            return HttpResponse(json.dumps(db5))
    except Exception as e:
        print("#@orderdetails: %s %s"%(mytime2(), e))
    return HttpResponse(db5)

def ordersReset():
    try:
        #db3 = db.productsapp_orderdetails.bulk_write([ DeleteMany({}) ])
        #print( db3.bulk_api_result )
        return 1
    except Exception as e:
        print("ordersReset %s %s")%(mytime2(), e)
    return -1

def dbreset(xyclient):
    try:
        xyclient.close()
    except Exception as e:
        print("#@dbreset: %s %s"%(mytime2(), e))
    return xyclient

def temp():
    rslt = {
        "productID": "0",
        "productName": "0",
        "supplierID": "0",
        "categories": { "categoryID": "0" },
        "quantityPerUnit": "0",
        "unitPrice": "0",
        "unitsInStock": "0",
        "unitsOnOrder": "0",
        "reorderLevel": "0",
        "discontinued": "0" }
    return rslt

def updateorders2(order):
    try:
        pid = str(order.productID)
        quantity = float(order.quantity)
        product = db.productsapp_products.find_one({"productID": pid})
        dbr = db.productsapp_products.bulk_write([
            UpdateOne({"productID": pid}, {"$set": {"unitsOnOrder": float(product["unitsOnOrder"])}}),
            UpdateOne({"productID": pid}, {"$inc": {"unitsOnOrder": float(quantity)}}, upsert=True)])
        return dbr
    except Exception as e:
        print("#@updateorders2: %s %s"%(mytime2(), e))
    return -1

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
