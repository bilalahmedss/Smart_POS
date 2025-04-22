from django.urls import path
from .views import login_view, register_user, otp_password_reset_request, otp_password_reset_verify
from django.contrib.auth.views import LogoutView

app_name = "authentication"
urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_user, name="register"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
         
    # OTP-based password reset URLs
    path('accounts/password-reset/', 
         otp_password_reset_request, 
         name='otp_password_reset_request'),
    path('accounts/password-reset/verify/', 
         otp_password_reset_verify, 
         name='otp_password_reset_verify'),
]
