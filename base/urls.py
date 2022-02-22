
from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('', views.getRoutes, name='routes'),

    path('users/register/', views.registerUser, name = 'register'),
    path('users/profile/', views.getUserProfile , name='users-profile'),
    path('users/', views.getUsers , name='users'),
    path('products/', views.getProducts , name='product'),
]
 