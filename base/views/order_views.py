''' 
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Product, Orders, OrderItem, ShippingAddress
from base.serializers import ProductSerializer
from rest_framework import status

'''