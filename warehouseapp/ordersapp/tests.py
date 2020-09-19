import unittest
from django.test import Client
import datetime
import time

# Create your tests here.

class OrdersAppTest(unittest.TestCase):
    def test_index(self):
        print("#")
        print("##############################################################")
        print("#")
        print("#00 Testing: Client, Content, Context.")
        print("#01: Test ordersapp index: %s"%(mytime2()))
        client = Client()
        response = client.get('/ordersapp/')
        print("#02: Test ordersapp index: %s %s"%(mytime2(), response))
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

    def test_orders(self):
        print("#")
        print("##############################################################")
        print("#")
        print(print("#01: Test orders: %s"%(mytime2())))
        client = Client()
        response = client.post('/ordersapp/orders', {
            'orderID': '202009919171880',
            'productID': '2020099101240',
            'unitPrice': '500.00',
            'quantity': '500',
            'discount': '20'})
        print("Response: %s"%(response.status_code))
        #self.assertEqual(response.status_code, 302)
        self.assertEqual(response.status_code, 200)

def mytime2():
    qrb = time.time()
    log2 = datetime.datetime.utcfromtimestamp(qrb)
    return log2
