
# from re import U
# from urllib.parse import urljoin
from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('vendor/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('', views.getRoutes, name='routes'),

    path('register/', views.registerUser, name = 'register'),
    path('profile/', views.getUserProfile , name='users-profile'),
    path('', views.getUsers , name='users'),

    path('allVendors/', views.getAllVendors , name='allVendors'),# test for vendors

    path('<str:pk>/', views.getUserById, name='user'),
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
]
