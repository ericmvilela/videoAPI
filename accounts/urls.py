from django.urls import path
from . import apis

urlpatterns = [
    path("register/", apis.RegisterApi.as_view(), name="register"),
    path("login/", apis.LoginApi.as_view(), name="login"),
    path('me/', apis.UserApi.as_view(), name='me'),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),
    path("edit/", apis.EditApi.as_view(), name="logout"),
]