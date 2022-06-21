
from django.urls import path, include

from base.views import  product_views as views


urlpatterns = [

    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('productsByCategory/<str:category>/', views.getProductsByCategory, name='getProductsByCategory'),
    

]


 
# n1_slug     api/category-products/products/n1_slug/
# http://127.0.0.1:8000/api/category-products/products/ClassicChevyBodyComponentsandGlass_slug/  # ClassicChevyBodyComponentsandGlass_slug
# http://127.0.0.1:8000/api/category-products/productsByCategory/12/  # with category id - works completely fine
