
# from re import U
# from urllib.parse import urljoin
from django.urls import path
#from base.views import *
from base.views import product_views as views


urlpatterns = [

    path('', views.getProducts, name='products'),

    path('createCategory/', views.createCategory, name='createCategory'), #createCategory/ added on 06.04.2022
    path('categories/', views.getCategories, name='get-categories'),
    path('deleteCategory/<str:pk>/', views.deleteCategory, name='deleteCategory'),

    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    # path('create/', views.createProduct, name='product-create'),

    # this was working perfectly, now testing-  path('categories/', views.getCategories, name='get-categories'),         #if we'll write this line of code then it'll not work, we have to keep this above of the '<str:pk>/' code.

    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    path('top/', views.getTopProducts, name='top-products'),
    path('<str:pk>/', views.getProduct, name='product'),  #<str:pk> #<int:pk> #<pk>
    
    path('productByVendorId/<str:pk>/', views.getProductByVendor, name='productByVendorId'), # Test for vendorId based Products

    path('update/<str:pk>/', views.updateProduct, name='product-update'),
    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),



]



# http://127.0.0.1:8000/api/products/?keyword=IMPERIAL   #this is working perfectly for the products search with keyword. 
# http://127.0.0.1:8000/api/products/?page=2   #this is working perfectly for the pagination.
# http://127.0.0.1:8000/api/products/?keyword=IMPERIAL&page=1   #this is working perfectly for the pagination.

# http://127.0.0.1:8000/api/products/?products_per_page=2  #this one is for the products_per_page based on a number selected by the user. And it works perfectly
# http://127.0.0.1:8000/api/products/?products_per_page=2&keyword=P&page=3  #this one is for "2 products per page" and "page 3" and "keyword P" and it perfectlly works.