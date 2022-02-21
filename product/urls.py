from django.urls import path, include
from .views import ProductsView, product, products
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('products', ProductsView, 'products')

urlpatterns = [
    path('', products, name="products"),
    path('/<id>', product, name="product"),
    # path('', include(router.urls)),
]