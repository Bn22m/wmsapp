from django_webtest import WebTest
from django.test import Client
from django.forms import DecimalField, ValidationError, Widget
import pymongo
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne
import json
import os
import os.path
import pprint
import datetime
import time
dbclient = MongoClient()
db = dbclient.nwwarehousedb
web = Client()
from infoserviceapp.models import mytime22
ddy = mytime22()
ddx = ddy

class TestWmsApp(WebTest):

    def setUp(self):
        try:
            web = Client()
            dt = mytime22()
            dydt = dt - ddx
            print("#00 setup: %s %s"%(dydt, self))
            print("##############################################################")
            print("#")
        except Exception as e:
            pprint.pprint("@test wms 00 setup: %s"%(e))

    def test01_suppliers(self):
        try:
            db1 = db.productsapp_suppliers
            db1 = resetDB(mytime2(), db1, 'suppliers')
            idb1 = db1.create_index([('supplierID', pymongo.ASCENDING)], unique=True)
            pprint.pprint(idb1)
            rdb1 = db1.insert_many(wmssuppliers("0"))
            pprint.pprint(rdb1)
            print("#")
            print("##############################################################")
            print("#")
            print("#")
            print("#01 test suppliers: %s"%(self))
            print("##############################################################")
            print("#01a")
            response = web.get('/productsapp/suppliers')
            pprint.pprint(response)
            print("#")
            print("##############################################################")
            print("#01b")
            db1 = db.productsapp_suppliers
            db1test = wmssuppliers("0")
            test1 = db1test[0]["supplierID"]
            test1a = db1.find_one({ "supplierID": test1 })
            pprint.pprint(test1a)
            assert(test1a["supplierID"] == test1)
            #test2 = test1a[0]["supplierID"]
            test2 = test1a["supplierID"]
            pprint.pprint(test1)
            pprint.pprint(test2)
            print("#")
            print("##############################################################")
            print("#01c")
            response2 = web.get('/suppliersapp/wsuppliers')
            pprint.pprint(response2)
            print("#")
            print("##############################################################")
            print("#01d")
        except Exception as e:
            pprint.pprint("@test wms01 suppliers: %s"%(e))

    def test02_category(self):
        try:
            db2 = db.productsapp_products
            db2 = resetDB(mytime2(), db2, 'products')
            idb2 = db2.create_index([('productID', pymongo.ASCENDING)], unique=True)
            pprint.pprint(idb2)
            rdb2 = db2.insert_many(wmsproducts("0"))
            pprint.pprint(rdb2)
            print("#")
            print("##############################################################")
            print("#")
            print("#02 test category: %s"%(self))
            print("##############################################################")
            print("#")
            response = web.get('/productsapp/checkcategories?pid=100020')
            pprint.pprint(response)
            print("#")
            print("##############################################################")
            print("#")
            db1 = db.productsapp_products
            db1test = wmsproducts("0")
            test1 = db1test[0]["categories"]["categoryID"]
            test1a = db1.find_one({ "productID": "100020" })
            pprint.pprint(test1)
            print("##############################################################")
            pprint.pprint(test1a)
            print("##############################################################")
            pprint.pprint(test1a["categories"])
            print("#")
            print("##############################################################")
            print("#")
            response2 = web.get('/productsapp/wproducts')
            pprint.pprint(response2)
            print("#")
            print("##############################################################")
            print("#")
        except Exception as e:
            pprint.pprint("@test wms02 cat: %s"%(e))

    def test03_orders(self):
        try:
            db3 = db.productsapp_orderdetails
            db3 = resetDB(mytime2(), db3, 'orders')
            idb3 = db3.create_index([('orderID', pymongo.ASCENDING)], unique=True)
            pprint.pprint(idb3)
            rdb3 = db3.insert_many(wmsorders("0"))
            pprint.pprint(rdb3)
            print("#")
            print("##############################################################")
            print("#")
            print("#")
            print("#03 test orders: %s"%(self))
            print("##############################################################")
            print("#03a")
            response1 = web.get('/productsapp/checkproducts?pid=100080')
            pprint.pprint(response1)
            print("#")
            print("##############################################################")
            print("#03b")
            response2 = web.get('/ordersapp/orderdetails?pid=20200831111204567')
            pprint.pprint(response2)
            print("#")
            print("##############################################################")
            print("#03c")
            print("#")
        except Exception as e:
            print("@test wms03 orders: %s"%(e))

    def test04_products(self):
        try:
            print("#")
            print("##############################################################")
            print("#")
            print("#04 test products: %s"%(self))
            print("##############################################################")
            print("#")
            db1 = db.productsapp_products
            pid = "100080"
            pid2 = str(pid)
            test1a = db1.find_one({ "productID": pid2 })
            pprint.pprint(test1a)
            test1b = test1a['unitsOnOrder']
            db2 = db.productsapp_orderdetails
            test2a = db2.find_one({ "orderID": "20200831111204567" })
            pprint.pprint(test2a)
            test2b = test2a["quantity"]
            test3a = (test1b + test2b)
            print("Test3a: %s + %s = %s"%(test1b, test2b, test3a))
            if (float(test3a) == float("1000")):
                print("# We are done. Thank you for Testing. Enjoy....")
            else:
                #>>> xy = float("500") + float("500")
                #>>> xy
                #1000.0
                #>>>
                test4a = float("500") + float("500")
                test4b = float(test1b)
                test4c = float(test2b)
                test4d = (test4b + test4c)
                print("Test4d: %s + %s = %s"%(test4b, test4c, test4d))
                print("##############################################################")
                assert(test4d == test4a)
                test4c = updateorders2(test2a)
                pprint.pprint(test4c)
                print("##############################################################")
                test5 = db1.find_one({ "productID": pid2 })
                pprint.pprint(test5)
                print("##############################################################")
                test6 = test5["unitsOnOrder"]
                print("unitsOnOrder = %s"%(test6))
                assert(float(test6) == float(test4a))
            print("#")
            print("##############################################################")
            print("#04")
            print("#")
            pprint.pprint(dbreset(dbclient))
            print("#@ We are done. Thank you for Testing. Enjoy...")
            print("#")
            print("##############################################################")
            print("#")
            print("#")
        except Exception as e:
            print(dbreset(dbclient))
            print("@test wms04 products: %s"%(e))

    def tearDown(self):
        try:
            print("#04 tear down %s"%(self))
            print("##############################################################")
            print("#")
            done = 0
            print("done: %s %s"%(mytime2(), done))
            print("#")
            print("##############################################################")
            print("#")
        except Exception as e:
            print("done: %s %s"%(mytime2(), e))

def wmsproducts(request):
    print("products: %s, %s"%(mytime2(), request))
    dbproducts = [
      {"productID": "100020","productName": "proWMS",
       "supplierID": "202008281031123",
       "categories": wmscategories(4),
       "quantityPerUnit": "100", "unitPrice": "250.00", "unitsInStock": "49",
       "unitsOnOrder": "100", "reorderLevel": "60", "discontinued": "False"},
      {"productID": "100030","productName": "proIS",
       "supplierID": "202008291431123",
       "categories": wmscategories(2),
       "quantityPerUnit": "300", "unitPrice": "3250.00", "unitsInStock": "249",
       "unitsOnOrder": "0", "reorderLevel": "50", "discontinued": "False"},
      {"productID": "100040", "productName": "proIoT",
       "supplierID": "202008301531123",
       "categories": wmscategories(0),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "749",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "100050", "productName": "proIoTv6",
       "supplierID": "202008291431123",
       "categories": wmscategories(1),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "749",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "100060", "productName": "proIT",
       "supplierID": "202008301531123",
       "categories": wmscategories(2),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "49",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "100080", "productName": "eoTv6",
       "supplierID": "202006291431123",
       "categories": wmscategories(3),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "29",
       "unitsOnOrder": "500", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "100070", "productName": "droIT",
       "supplierID": "202005301531123",
       "categories": wmscategories(5),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "40",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"}
    ]
    return dbproducts

def wmscategories(request):
    print("categories: %s, %s"%(mytime2(), request))
    dbcategories = [
        {"categoryID": "dtsd2", "categoryName": "Cool",
         "description": "Cool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5orange.jpg"},
        {"categoryID": "dtiot7", "categoryName": "Iot DIY",
         "description": "0DIY category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5pink.jpg"},
        {"categoryID": "dtis6", "categoryName": "Green Energy",
         "description": "Green category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5green.jpg"},
        {"categoryID": "dtmd2", "categoryName": "Awesome",
         "description": "Awesome category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5purple.jpg"},
        {"categoryID": "dtis4", "categoryName": "IS cool",
         "description": "IS cool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5purple.jpg"},
        {"categoryID": "dtds6", "categoryName": "DS Cool",
         "description": "DS Cool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5orange.jpg"}
    ]
    return dbcategories[request]

def wmssuppliers(request):
    print("suppliers: %s, %s"%(mytime2(), request))
    dbsuppliers = [
      { "supplierID": "202008281031123", "companyName": "Ran Group",
        "contactName": "Jo Ben", "contactTitle": "Sir",
        "address": "29 Ran Avenue", "city": "My New City", "region": "West",
        "postalCode": "1234", "country": "New Galexyiya",
        "phone": "012345678900", "fax": "012345678901",
        "homePage": "https://rangroup.sup" },
      { "supplierID": "202008291431123", "companyName": "Cool Group",
        "contactName": "Top Ben", "contactTitle": "Dr",
        "address": "29 Cool Avenue", "city": "My New City", "region": "West",
        "postalCode": "1234", "country": "New Galexyiya",
        "phone": "032345678900", "fax": "032345678901",
        "homePage": "https://coolroup.sup" },
      { "supplierID": "202008301531123", "companyName": "Awesome Group",
        "contactName": "Ben Ben", "contactTitle": "Pro",
        "address": "890 Awesome Drive", "city": "My New City", "region": "West",
        "postalCode": "1234", "country": "New Galexyiya",
        "phone": "042345678900", "fax": "042345678901",
        "homePage": "https://awesomegroup.sup" },
      { "supplierID": "202006291431123", "companyName": "Super Group",
        "contactName": "Ro Ro", "contactTitle": "Miss",
        "address": "290 Super Avenue", "city": "My New City", "region": "West",
        "postalCode": "1234", "country": "New Galexyiya",
        "phone": "052345678900", "fax": "052345678901",
        "homePage": "https://supergroup.sup" },
      { "supplierID": "202005301531123", "companyName": "Tech seg",
        "contactName": "Don Donen", "contactTitle": "Mr",
        "address": "29 Ran Avenue", "city": "My New City", "region": "West",
        "postalCode": "1234", "country": "New Galexyiya",
        "phone": "017345678900", "fax": "017345678901",
        "homePage": "https://rangroup.sup" }
    ]
    return dbsuppliers

def wmsorders(request):
    print("orders: %s, %s"%(mytime2(), request))
    dborders = [
      { "orderID": "20200831101234567", "productID": "100020",
        "unitPrice": "250.00", "quantity": "100", "discount": "10" },
      { "orderID": "20200831111204567", "productID": "100080",
        "unitPrice": "350.00", "quantity": "500", "discount": "10" }
    ]
    return dborders

def resetDB(request, coll, xb):
    try:
        #db2 = dbclient.get_database()
        #print(db2.name)
        #assert(db2.name == 'nwwarehousedb')
        dup = dbbackUp(coll, xb)
        print("#02 resetDB: %s %s %s %s"%(request, coll, xb, dup))
        coll.drop()
        return coll
    except Exception as e:
        print("#00 resetDB: %s %s"%(request, xb))
    return coll

def serialN():
    d2 = mytime2()
    d3 = d2.microsecond
    qrc = "%s%s%s%s%s%s%s"%(d2.year, d2.month, d2.day,
        d2.hour, d2.minute, d2.second, d3%1000)
    return qrc

def dbbackUp(dbcoll, xb):
    try:
        #dbtxt1 = "productsapp/dbdata/%s%s.json"%(xb, serialN())
        dbtxt = "dbdataapp/static/dbdataapp/dbdata/%s%s.json"%(xb, serialN())
        print(dbtxt)
        db3 = []
        db4 = dbcoll.find()
        x = 0
        for xy in db4:
            db3.append(xy)
            db3[x]['_id'] = "%s"%(db3[x]['_id'])
            x += 1
        #db5 = json.dumps(db3)
        with open(dbtxt, 'w') as f:
            json.dump(db3, f)
        #print(db5)
        print("#01 dbbackUp: %s %s"%(mytime2(), x))
        return db3
    except Exception as e:
        print("@dbbackUp: %s %s"%(mytime2(), e))
    return -1

def dbreset(dxclient):
    try:
        dxclient.close()
    except Exception as e:
        print("#@dbreset: %s %s"%(mytime2(), e))
    return dxclient

def updateorders2(order):
    try:
        pid = str(order["productID"])
        quantity = float(order["quantity"])
        xproduct = db.productsapp_products.find_one({"productID": pid})
        pprint.pprint(xproduct)
        dbr = db.productsapp_products.bulk_write([
            UpdateOne({"productID": pid}, {"$set": {"unitsOnOrder": float(xproduct["unitsOnOrder"])}}),
            UpdateOne({"productID": pid}, {"$inc": {"unitsOnOrder": float(quantity)}}, upsert=True)])
        return dbr
    except Exception as e:
        print("#@updateorders2: %s %s"%(mytime2(), e))
    return -1

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
