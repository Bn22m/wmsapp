from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wms', views.index, name='index'),
    path('products', views.products, name='products'),
    path('orders', views.orders, name='orders'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('categories', views.categories, name='categories'),
]
