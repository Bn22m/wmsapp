from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('checksuppliers', views.checksuppliers, name='checksuppliers'),
    path('wsuppliers', views.wsuppliers, name='wsuppliers'),
]
