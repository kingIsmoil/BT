from django.urls import path
from .views import UserListAPIView, RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("logout/", LogoutAPIView.as_view(), name="user-logout"),
]
