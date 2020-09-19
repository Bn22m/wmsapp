import unittest
from django.test import Client
import datetime
import time

# Create your tests here.

class SuppliersAppTest(unittest.TestCase):

    def test_index(self):
        print("#")
        print("##############################################################")
        print("#")
        print("#00 Testing: Client, Content, Context.")
        print("#01: Test supplier index: %s"%(mytime2()))
        client = Client()
        response = client.get('/suppliersapp/')
        print("#02: Test suppliersapp index: %s %s"%(mytime2(), response))
        print("Client: %s"%(response.client))
        print("#")
        print("##############################################################")
        print("#")
        print("#03: ")
        print("Content: %s"%(response.content))
        print("#")
        print("##############################################################")
        print("#")
        print("#04: ")
        print("Context: %s"%(response.context))
        print("#")
        print("##############################################################")
        print("#")
        print("#05: ")
        print("Response: %s"%(response.status_code))
        print("#")
        print("##############################################################")
        print("#")
        self.assertEqual(response.status_code, 200)

    def test_suppliers(self):
        print("#")
        print("##############################################################")
        print("#")
        print(print("#01: Test suppliers: %s"%(mytime2())))
        client = Client()
        response = client.post('/suppliersapp/suppliers', {
            'supplierID': '2020099945333', 'companyName': 'Nse suppliers',
            'contactName': 'Seal One', 'contactTitle': 'Mnr',
            'address': '44 Nse Avenue', 'city': 'Hope City', 'region': 'South',
            'postalCode': '4200', 'country': 'New Galexoya',
            'phone': '022 345 678900', 'fax': '022 345 678901',
            'homePage': 'http://nsesuppliers.supp'})
        print("Response: %s"%(response.status_code))
        #self.assertEqual(response.status_code, 302)
        self.assertEqual(response.status_code, 200)

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
