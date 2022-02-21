from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Chain
from rest_framework import viewsets, status
from .serializers import ChainSerializer


# testing view
class ChainsView(viewsets.ModelViewSet):
    serializer_class = ChainSerializer
    queryset = Chain.objects.all()


# Create your views here.
@api_view(['GET', 'POST'])
def chains(request):
    if request.method == 'GET':
        chains = Chain.objects.all()
        chains_serializer = ChainSerializer(chains, many=True)
        return JsonResponse(chains_serializer.data, safe=False)
    elif request.method == 'POST':
        chain_data = JSONParser().parse(request)
        chain_serializer = ChainSerializer(data=chain_data)
        if chain_serializer.is_valid():
            chain_serializer.save()
            return JsonResponse(chain_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(chain_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def chain(request, id):
    chain = Chain.objects.get(id=id)
    if request.method == 'GET':
        chain_serializer = ChainSerializer(chain)
        return JsonResponse(chain_serializer.data)
    elif request.method == 'PUT':
        chain_data = JSONParser().parse(request)
        chain_serializer = ChainSerializer(chain, chain_data)
        if chain_serializer.is_valid():
            chain_serializer.save()
            return JsonResponse(chain_serializer.data)
        return JsonResponse(chain_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        chain.delete()
        return JsonResponse({'message': 'Chain was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



