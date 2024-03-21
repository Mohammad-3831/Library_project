from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', GetAllUsersView.as_view(), name='get_all_users'),
    path('user/<int:pk>', GetUserView.as_view(), name='get_users'),
    path('add', AddUserView.as_view(), name='add_users'),
    path('update', UpdateUserView.as_view(), name='update_users'),
    path('delete', DeleteUserView.as_view(), name='delete_users'),
]



# کپی پیست می کنی کووووووووووون گشاددددددد حواست باشه کووووووووووووووووووونییییییییییییییییییییییییییییییییییییییییییییییییییییییییییست