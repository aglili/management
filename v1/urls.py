from django.urls import path
from accounts import views


urlpatterns = [
    path("sign-up",views.user_sign_up,name="user-sign-up"),
    path("login",views.user_login,name="user-login"),
]