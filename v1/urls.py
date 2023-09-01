from django.urls import path
from accounts import views


urlpatterns = [
    path("sign-up",views.user_sign_up,name="user-sign-up"),
    path("login",views.user_login,name="user-login"),
    path("password-reset",views.request_password_reset,name="request-password-reset"),
    path("verify-otp",views.verify_otp,name="verify_otp"),
    path("new-password",views.change_password,name="reset-to-new-password")
]