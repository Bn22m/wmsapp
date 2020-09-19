#from django.db import models
from djongo import models
from django import forms

# Create your models here.

class Suppliers(models.Model):
    supplierID = models.CharField(max_length=250, unique=True)
    companyName = models.CharField(max_length=250)
    contactName = models.CharField(max_length=250)
    contactTitle = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    postalCode = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    fax = models.CharField(max_length=250)
    homePage = models.URLField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.companyName

class Categories(models.Model):
    categoryID = models.CharField(max_length=250, unique=True)
    categoryName = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.categoryName

    class Meta:
        abstract = True

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = (
           'categoryID', 'categoryName', 'description', 'picture'
        )

class Products(models.Model):
    productID = models.CharField(max_length=250, unique=True)
    productName = models.CharField(max_length=250)
    supplierID = models.CharField(max_length=250)
    categories = models.EmbeddedField(
        model_container=Categories,
        model_form_class=CategoriesForm
    )
    quantityPerUnit = models.DecimalField(max_digits=9, decimal_places=2)
    unitPrice = models.DecimalField(max_digits=9, decimal_places=2)
    unitsInStock = models.DecimalField(max_digits=9, decimal_places=2)
    unitsOnOrder = models.DecimalField(max_digits=9, decimal_places=2)
    reorderLevel = models.DecimalField(max_digits=9, decimal_places=2)
    discontinued = models.BooleanField(default=False)
    objects = models.DjongoManager()

    def __str__(self):
        return self.productName

class OrderDetails(models.Model):
    orderID = models.CharField(max_length=250, unique=True)
    productID = models.CharField(max_length=250)
    unitPrice = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    objects = models.DjongoManager()

    def __str__(self):
        return self.orderID
