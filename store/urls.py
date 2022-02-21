from django.urls import path, include
from .views import StoresView, stores, store
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('stores', StoresView, 'stores')

urlpatterns = [
    path('', stores, name="stores"),
    path('/<id>', store, name="store"),
    # path('', include(router.urls)),
]