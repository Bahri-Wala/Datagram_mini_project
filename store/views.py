from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import StoreSerializer
from .models import Store


# testing view
class StoresView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# Create your views here.
@api_view(['GET', 'POST'])
def stores(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        stores_serializer = StoreSerializer(stores, many=True)
        return JsonResponse(stores_serializer.data, safe=False)
    elif request.method == 'POST':
        store_data = JSONParser().parse(request)
        store_serializer = StoreSerializer(data=store_data)
        if store_serializer.is_valid():
            store_serializer.save()
            return JsonResponse(store_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def store(request, id):
    store = Store.objects.get(id=id)
    if request.method == 'GET':
        store_serializer = StoreSerializer(store)
        return JsonResponse(store_serializer.data)
    elif request.method == 'PUT':
        store_data = JSONParser().parse(request)
        store_serializer = StoreSerializer(store, store_data)
        if store_serializer.is_valid():
            store_serializer.save()
            return JsonResponse(store_serializer.data)
        return JsonResponse(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        store.delete()
        return JsonResponse({'message': 'Store was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

