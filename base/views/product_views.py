from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Product
from base.serializers import ProductSerializer
from rest_framework import status



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


## Get Product View
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)     #(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
