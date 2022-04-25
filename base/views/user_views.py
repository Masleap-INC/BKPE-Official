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



# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])  
# def getRoutes(request):
#     routes = [
#         '/api/products',
#     ]
#     return Response(routes)




@api_view(['GET'])
# need to add later  @permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['GET'])
# need to add later  @permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
# need to add later  @permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)





@api_view(['PUT'])
# need to add later  @permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)






@api_view(['DELETE'])
# need to add later  @permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')


# #get superuser
# @api_view(['GET'])
# def getSuperUser(request):
#     user = User.objects.get(is_superuser=True)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


## get all Vendors view
@api_view(['GET'])
def getAllVendors(request):
    vendors = User.objects.filter(is_staff=True)
    serializer = UserSerializer(vendors, many=True)
    return Response(serializer.data)

''' 

# test for vendor by id
 
def getVendor(request):
    vendors = User.objects.filter(is_staff=True)
    serializer = UserSerializer(vendors, many=True)
    return Response(serializer.data)

def getVendorById(request, pk):
    vendor = User.objects.get(id=pk)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByEmail(request, email):
    vendor = User.objects.get(email=email)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByName(request, name):
    vendor = User.objects.get(first_name=name)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByUsername(request, username):
    vendor = User.objects.get(username=username)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByPhone(request, phone):
    vendor = User.objects.get(phone=phone)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByAddress(request, address):
    vendor = User.objects.get(address=address)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByCity(request, city):
    vendor = User.objects.get(city=city)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByState(request, state):
    vendor = User.objects.get(state=state)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)


def getVendorByZip(request, zip):
    vendor = User.objects.get(zip=zip)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByCountry(request, country):
    vendor = User.objects.get(country=country)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByCompany(request, company):
    vendor = User.objects.get(company=company)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByWebsite(request, website):
    vendor = User.objects.get(website=website)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByDescription(request, description):
    vendor = User.objects.get(description=description)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def getVendorByLogo(request, logo):
    vendor = User.objects.get(logo=logo)
    serializer = UserSerializer(vendor, many=False)
    return Response(serializer.data)

def vendorLogin(request):
    data = request.data
    email = data['email']
    password = data['password']
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        else:
            message = {'detail': 'Invalid password'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'detail': 'User with this email does not exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

def vendorRegister(request):
    data = request.data
    email = data['email']
    password = data['password']
    try:
        user = User.objects.get(email=email)
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        user = User.objects.create_user(email=email, password=password)
        user.is_staff = True
        user.save()
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

def vendorUpdate(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

def vendorDelete(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')

 

def vendorProfileUpdate(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

'''

