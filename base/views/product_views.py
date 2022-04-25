from itertools import product
from pydoc import describe
#from socket import RDS_RDMA_SILENT
from unicodedata import category, name
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Product,Category, Review
from base.serializers import ProductSerializer,CategorySerializer
from rest_framework import status
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView



## Custom Permissions only for superuser
class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser





@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):

    Total_Products = request.query_params.get('products_per_page')
    if Total_Products == '1':
        NoOfProducts = 1
    elif Total_Products == '2':
        NoOfProducts = 2
    elif Total_Products == '3':
        NoOfProducts = 3
    elif Total_Products == '4':
        NoOfProducts = 4
    else:
        NoOfProducts = 6



    query = request.query_params.get('keyword')
    print('query:', query)
    if query == None:
        query = ''
    products = Product.objects.filter(name__icontains=query)

    # Pagination starts here

    #NoOfProducts = 4
    page = request.query_params.get('page')
    paginator = Paginator(products, NoOfProducts) #(products, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)

    # Pagination ends here

    # products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # return Response(serializer.data)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})







'''    
##### This one is the old getProducts view which works perfectly.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    query = request.query_params.get('keyword')
    print('query:', query)
    if query == None:
        query = ''
    products = Product.objects.filter(name__icontains=query)

    # Pagination starts here

    NoOfProducts = 4
    page = request.query_params.get('page')
    paginator = Paginator(products, NoOfProducts) #(products, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)

    # Pagination ends here

    # products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # return Response(serializer.data)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})

'''

@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)







## Get Product by Product id View
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)     #(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


## Get Product by Product Vendor id View
@api_view(['GET'])
def getProductByVendor(request, pk):
    products = Product.objects.filter(vendor_id=pk)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




@api_view(['POST'])
# need to add later  @permission_classes([IsAdminUser])
def createProduct(request):
    #user = request.user
    vendor = request.user

    product = Product.objects.create(
        #user=user,
        vendor=vendor,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(id=pk)

    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


## Delete Product View
@api_view(['DELETE'])
# need to add later  @permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)     #(_id=pk)
    product.delete()
    return Response('Product Deleted')



## Upload Image View while Updating Product
@api_view(['POST'])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(id=product_id)  #(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')



## Create Category View    #createCategory/ added on 06.04.2022
@api_view(['POST'])
@permission_classes([IsSuperUser])
def createCategory(request):
    data = request.data
    category = Category.objects.create(
        name=data['name'],
        slug = data['slug']
    )

    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


## Delete Category View
@api_view(['DELETE'])
@permission_classes([IsSuperUser])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)     #(_id=pk)
    category.delete()
    return Response('Category Deleted')







@api_view(['GET'])
def getCategories(request):   #pk
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# ## Test view for Category based product
# @api_view(['GET'])
# def getCategorybasedProducts(request,pk):
#     products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# # Starting View of Category inspired by Amazone YouTube Tutorial

# class ProductListAPIVIew(ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     filter_fields = (
#         'category__id',
#     )
#     search_fields = (
#         'title',
#     )


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)





@api_view(['POST'])
#@permission_classes([IsAuthenticated])
#@permission_classes([IsAdminUser])
def createProductReview(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)  #_id
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}

        #reviews = product.review_set.all()
        #numReviews1 = len(reviews)
        #product.save()
        #return Response({numReviews1})

        return Response(content , status=status.HTTP_400_BAD_REQUEST) 

    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,     #user.first_name
            rating=data['rating'],
            comment=data['comment'],
        )
        #return Response('Review Added')
        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()

        return Response('Review Added')


        

''' 
        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()

        return Response('Review Added')

'''















# ''' 
# @api_view(['GET'])     ##To be deleted later
# @permission_classes([IsAuthenticated])
# def getOrderById(request, pk):

#     user = request.user

#     try:
#         order = Order.objects.get(id=pk)
#         if user.is_staff or order.user == user:
#             serializer = OrderSerializer(order, many=False)
#             return Response(serializer.data)
#         else:
#             Response({'detail': 'Not authorized to view this order'},
#                      status=status.HTTP_400_BAD_REQUEST)
#     except:
#         return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)

# '''
# @api_view(['GET'])     ##To be deleted later
# @permission_classes([IsAuthenticated])
# def getCatProd(request, pk):

''' 
class productList(generics.ListAPIView):
   serializer_class = productSerializer
   def get_queryset(self):
       queryset = Product.objects.all()
       search = self.request.query_params.get('search', None)
       if search is not None:
           queryset = queryset.filter(product_name__icontains=search)
'''
'''
## Get Product View
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)     #(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

'''
'''
@api_view(['GET'])
def productList(request, pk):
    queryset = Product.objects.all(product_category_id = pk )    (id = pk) #id=product_id
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
'''

