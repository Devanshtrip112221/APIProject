from django.urls import path
from Home.views import ProductCRUDCBV

urlpatterns = [
     path('api/products/', ProductCRUDCBV.as_view(), name='product-crud'),
]