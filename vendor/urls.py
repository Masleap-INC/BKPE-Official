from django.urls import path
from base.views import user_views as user_views

urlpatterns = [
    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', user_views.registerUser, name = 'register'),


    # path('profile/', user_views.getUserProfile , name='users-profile'),
    # path('', user_views.getUsers , name='users'),
    # path('<str:pk>/', user_views.getUserById, name='user'),
    path('update/<str:pk>/', user_views.updateUser, name='user-update'),
    # path('delete/<str:pk>/', user_views.deleteUser, name='user-delete'),


]