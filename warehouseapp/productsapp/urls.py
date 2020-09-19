from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wproducts', views.wproducts, name='wproducts'),
    path('newproduct', views.newproduct, name='newproduct'),
    path('newproducts', views.newproducts, name='newproducts'),
    path('updateproducts', views.updateproducts, name='updateproducts'),
    path('getproducts', views.getproducts, name='getproducts'),
    path('checkproducts', views.checkproducts, name='checkproducts'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('checkcategories', views.checkcategories, name='checkcategories'),
    path('updateorders', views.updateorders, name='updateorders'),
]
