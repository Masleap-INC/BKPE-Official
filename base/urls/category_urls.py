
from django.urls import path, include

from base.views import  product_views as views

urlpatterns = [

    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    

]


 
# n1_slug     api/category-products/products/n1_slug/

