from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
import os
import os.path
import unittest
from django.test import Client
import datetime
import time
import pprint


# Create your tests here.

class ProductsAppTest(unittest.TestCase):

    def test_newproducts(self):
        print("#")
        print("##############################################################")
        print("#")
        print("# 01: Test productsapp/newproducts: %s"%(mytime2()))
        print("#")
        client = Client()
        db = 0
        with open('productsapp/pdata/d5pink.jpg', 'rb') as fp:
            db += 1
            print(db)
            response = client.post('/productsapp/newproducts', {
                'productID': '2020099101240',
                'productName': 'Test Cool hat',
                'supplierID': '2020099945333',
                'categoryID': '485250494849575748504850',
                'categoryName': 'Test Red panel',
                'description': 'Multipupose hat for in doors and out doors use.',
                'picture': 'd5pink.jpg',
                'filename': fp,
                'quantityPerUnit': '100',
                'unitPrice': '100.00',
                'unitsInStock': '20',
                'unitsOnOrder': '500',
                'reorderLevel': '50',
                'discontinued': 'False'})
        print("Response: %s"%(response.status_code))
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        print("#")
        print("##############################################################")
        print("#")
        print("#00 Testing: Client, Content, Context.")
        print("#01: Test products index: %s"%(mytime2()))
        client = Client()
        response = client.get('/productsapp/')
        print("#02: Test p index: %s %s"%(mytime2(), response))
        print("Client: %s"%(response.client))
        print("#")
        print("##############################################################")
        print("#")
        print("#03: ")
        pprint.pprint("Content: %s"%(response.content))
        print("#")
        print("##############################################################")
        print("#")
        print("#04: ")
        pprint.pprint("Context: %s"%(response.context))
        print("#")
        print("##############################################################")
        print("#")
        print("#05: ")
        print("Response: %s"%(response.status_code))
        print("#")
        print("##############################################################")
        print("#")
        self.assertEqual(response.status_code, 200)

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
