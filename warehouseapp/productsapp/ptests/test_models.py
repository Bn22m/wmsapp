from django.test import TestCase
from productsapp.models import Suppliers, Products, OrderDetails
import datetime
import time


class SuppliersModelTest(TestCase):

    def setUpTestData(self):
        s = Suppliers()
        print("#")
        print("##############################################################")
        print("#")
        print("Testing Supplier Model: %s"%(mytime2()))
        s.supplierID='202009817253127'
        s.companyName='WMS suppliers'
        s.contactName='Deal Vone'
        s.contactTitle='Mnu'
        s.address='34 Wms Avenue'
        s.city='New Supplier City'
        s.region='West'
        s.postalCode='4200',
        s.country='New Galexoya'
        s.phone='012 345 678900'
        s.fax='012 345 678901'
        s.homePage='http://wmssuppliers.supp'
        print(s.companyName)
        self.assertEqual(s.companyName, 'WMS suppliers')
        pdate = mytime2()
        print("Saving: %s, %s"%(s, pdate))
        checks = checkSupplierID(s)
        if( checks["supplierID"] == "None" ):
            s.save()
        print(checks)

class ProductsModelTest(TestCase):

    def setUpTestData(self):
        p = Products()
        print("#")
        print("##############################################################")
        print("#")
        print("Testing Products Model: %s"%(mytime2()))
        p.productID = '20200981758138'
        p.productName = 'Willon panel'
        p.supplierID = '202009817253127'
        p.categories.categoryID = '56514956535549565748504850'
        p.categories.categoryName = 'Test Grean panel'
        p.categories.description = 'Multipupose panel for in doors and out doors use.'
        p.categories.picture = '/categoriesapp/cpicture/test56514956535549565748504850.jpg'
        p.quantityPerUnit = '500'
        p.unitPrice = '1000.00'
        p.unitsInStock = '9'
        p.unitsOnOrder = '50'
        p.reorderLevel = '10'
        p.discontinued='False'
        print(p.productName)
        self.assertEqual(p.discontinued, 'False')
        pdate = mytime2()
        print("Saving new product: %s %s"%(p, pdate))
        ckp = checkProductID(p)
        if( ckp["productID"] == "None" ):
            p.save()
        print(ckp)

class OrderDetailsModelTest(TestCase):

    def setUpTestData(self):
        o = OrderDetails()
        print("#")
        print("##############################################################")
        print("#")
        print("Testing OrderDetails Model: %s"%(mytime2()))
        o.orderID = '202009101358138'
        o.productID = '20200981758138'
        o.unitPrice = '500.00'
        o.quantity = '50.00'
        o.discount = '20.00'
        print(o.orderID)
        self.assertEqual(o.orderID, '202009101358138')
        pdate = mytime2()
        print("Saving Orders Details: %s %s"%(o, pdate))
        checks = checkOrderID(o)
        if( checks["orderID"] == "None" ):
            o.save()
        print(checks)

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2

def checkSupplierID(app):
    try:
        db3 = db.productsapp_suppliers.find_one({ "supplierID": app.supplierID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.supplierID))
        return { "supplierID": db3["supplierID"] }
    except Exception as e:
        print("checkSupplierID: %s %s"%(mytime2(), e))
    return { "supplierID": "None" }

def checkProductID(app):
    try:
        db3 = db.productsapp_products.find_one({ "productID": app.productID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.productID))
        return { "productID": db3["productID"] }
    except Exception as e:
        print("checkProductID: %s %s"%(mytime2(), e))
    return { "productID": "None" }

def checkOrderID(app):
    try:
        db3 = db.productsapp_orderdetails.find_one({ "orderID": app.orderID })
        print("db3: %s, %s, %s"%(mytime2(), db3, app.orderID))
        return { "orderID": db3["orderID"] }
    except Exception as e:
        print("checkOrderID: %s %s"%(mytime2(), e))
    return { "orderID": "None" }
