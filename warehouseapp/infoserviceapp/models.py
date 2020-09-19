from django.db import models
import datetime
import time
from django.utils import timezone

# Create your models here.

class InformationService(models.Model):
    orders = models.CharField(max_length=200)
    products = models.CharField(max_length=200)
    suppliers = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    picture = models.CharField(max_length=200)
    orderdate = models.DateTimeField()
    duedate = models.DateTimeField()
    deliverydate = models.DateTimeField()
    closed = models.BooleanField(default=True)
    info = models.TextField()
    logs = models.TextField()

    def isminfo(self):
        arg = {'id': '10002','name': 'WMS',
               'description': 'Warehouse Management System.', 'info': 'wms'}
        return info2(arg)

    def wsproducts(self):
        return(wmsproducts(mytime22()))

    def wssuppliers(self):
        return(wmssuppliers(mytime22()))

    def wsorders(self):
        return(wmsproducts(mytime22()))

    def mytime(self):
        return mytime22()

def mytime2():
    now = datetime.datetime.now()
    return now

def mytime22():
    now = mytime2()
    return timezone.make_aware(now)

def info2(arg):
    info3 = [arg, {'id': '10003', 'name': 'Orders', 'description': 'Order Details.', 'info': 'orders'},
        {'id': '10004', 'name': 'Products', 'description': 'Products.', 'info': 'products'},
        {'id': '10005', 'name': 'Suppliers', 'description': 'Suppliers.', 'info': 'suppliers'},
        {'id': '10006', 'name': 'Categories', 'description': 'Categories.', 'info': 'categories'},
        {'id': '10007', 'name': 'NewProducts', 'description': 'New Products.', 'info': 'newproduct'},
    ]
    return info3

def wmsproducts(request):
    print("products: %s"%(request))
    dbproducts = [
      {"productID": "110002","productName": "pproWMS",
       "supplierID": "202008281031123",
       "suppliers_id": {"supplierIDr": "202008281031123"},
       "categories": wmscategories(4),
       "quantityPerUnit": "100", "unitPrice": "250.00", "unitsInStock": "49",
       "unitsOnOrder": "100", "reorderLevel": "60", "discontinued": "False"},
      {"productID": "110003","productName": "pproIS",
       "supplierID": "202008291431123",
       "suppliers_id": {"supplierIDr": "202008291431123"},
       "categories": wmscategories(2),
       "quantityPerUnit": "300", "unitPrice": "3250.00", "unitsInStock": "249",
       "unitsOnOrder": "0", "reorderLevel": "50", "discontinued": "False"},
      {"productID": "110004", "productName": "pproIoT",
       "supplierID": "202008301531123",
       "suppliers_id": {"supplierIDr": "202008301531123"},
       "categories": wmscategories(0),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "749",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "110005", "productName": "pproIoTv6",
       "supplierID": "202008291431123",
       "suppliers_id": {"supplierIDr": "202008291431123"},
       "categories": wmscategories(1),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "749",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "110006", "productName": "pproIT",
       "supplierID": "202008301531123",
       "suppliers_id": {"supplierIDr": "202008301531123"},
       "categories": wmscategories(2),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "49",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "110008", "productName": "peoTv6",
       "supplierID": "202006291431123",
       "suppliers_id": {"supplierIDr": "202006291431123"},
       "categories": wmscategories(3),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "29",
       "unitsOnOrder": "500", "reorderLevel": "30", "discontinued": "False"},
      {"productID": "110007", "productName": "pdroIT",
       "supplierID": "202005301531123",
       "suppliers_id": {"supplierIDr": "202005301531123"},
       "categories": wmscategories(5),
       "quantityPerUnit": "500", "unitPrice": "350.00", "unitsInStock": "90",
       "unitsOnOrder": "0", "reorderLevel": "30", "discontinued": "False"}
    ]
    return dbproducts

def wmscategories(request):
    print("categories: %s"%(request))
    dbcategories = [
        {"categoryID": "psd2", "categoryName": "Cool",
         "description": "pCool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5orange.jpg"},
        {"categoryID": "piot7", "categoryName": "Iot DIY",
         "description": "pDIY category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5pink.jpg"},
        {"categoryID": "pis6", "categoryName": "Green Energy",
         "description": "Green category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5green.jpg"},
        {"categoryID": "pmd2", "categoryName": "Awesome",
         "description": "Awesome category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5purple.jpg"},
        {"categoryID": "pis4", "categoryName": "IS cool",
         "description": "IS cool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5purple.jpg"},
        {"categoryID": "pds6", "categoryName": "DS Cool",
         "description": "pDS Cool category with cool look and feel.",
         "picture": "categoriesapp/cpicture/d5orange.jpg"}
    ]
    return dbcategories[request]

def wmssuppliers(request):
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
    dborders = [
      { "orderID": "20200831101234567", "productID": "100020",
        "unitPrice": "250.00", "quantity": "100", "discount": "10" },
      { "orderID": "20200831111204567", "productID": "100080",
        "unitPrice": "350.00", "quantity": "500", "discount": "10" }
    ]
    return dborders

def serialn():
    d2 = mytime22()
    d3 = d2.microsecond
    qrc = "%s%s%s%s%s%s%s"%(d2.year, d2.month, d2.day,
        d2.hour, d2.minute, d2.second, d3%1000)
    return qrc
