from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "authentication"
urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_user, name="register"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path('accounts/password-reset/', 
         PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             html_email_template_name='accounts/password_reset_email.html',
             success_url='/accounts/password-reset/done/'
         ),
         name='password_reset'),
    path('accounts/password-reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html',
             success_url='/accounts/reset/done/'
         ),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
