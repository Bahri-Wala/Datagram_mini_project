from django.urls import path, include
from .views import ChainsView, chain, chains
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('chainsview', ChainsView, 'chains')

urlpatterns = [
    path('', chains, name="chains"),
    path('/<id>', chain, name="chain"),
    # path('', include(router.urls)),
]