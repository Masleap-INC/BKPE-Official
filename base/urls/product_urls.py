
# from re import U
# from urllib.parse import urljoin
from django.urls import path
#from base.views import *
from base.views import product_views as views


urlpatterns = [

    path('', views.getProducts, name='products'),
    path('categories/', views.getCategories, name='get-categories'),

    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    # path('create/', views.createProduct, name='product-create'),

    # this was working perfectly, now testing-  path('categories/', views.getCategories, name='get-categories'),         #if we'll write this line of code then it'll not work, we have to keep this above of the '<str:pk>/' code.

    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    path('<str:pk>/', views.getProduct, name='product'),  #<str:pk> #<int:pk> #<pk>

    path('update/<str:pk>/', views.updateProduct, name='product-update'),
    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),


]



