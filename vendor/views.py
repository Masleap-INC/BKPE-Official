from django.shortcuts import render


from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password



from vendor.serializers import VendorProfileSerializer
from vendor.models import VendorProfile

# Create your views here.


# Create Vendor Profile View
@api_view(['POST'])
def createVendorProfile(request):

    user = request.user

    vendor = VendorProfile.objects.create(
    user=user,
    name='Sample Name',
    address='Sample Address',
    city='Sample City',
    state='Sample State',
    zipcode='Sample Zipcode',
    country='Sample Country',
    phone='Sample Phone',
    email='Sample Email',
    #website='Sample Website'
    )  

    serializer = VendorProfileSerializer(vendor, many=False)
    return Response(serializer.data)

# Get Vendor Profile View
@api_view(['GET'])
def getVendorProfile(request):
    user = request.user
    vendor = VendorProfile.objects.get(user=user)
    serializer = VendorProfileSerializer(vendor, many=False)
    return Response(serializer.data)


# Update Vendor Profile View
@api_view(['PUT'])
def updateVendorProfile(request):
    user = request.user
    vendor = VendorProfile.objects.get(user=user)

    data = request.data

    vendor.name = data['name']
    vendor.address = data['address']
    vendor.city = data['city']
    vendor.state = data['state']
    vendor.zipcode = data['zipcode']
    vendor.country = data['country']
    vendor.phone = data['phone']
    vendor.email = data['email']
    #vendor.website = data['website']

    vendor.save()

    serializer = VendorProfileSerializer(vendor, many=False)
    return Response(serializer.data)


# Delete Vendor Profile View
@api_view(['DELETE'])
def deleteVendorProfile(request):
    user = request.user
    vendor = VendorProfile.objects.get(user=user)
    vendor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  
    





