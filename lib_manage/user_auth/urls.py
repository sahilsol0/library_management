from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from .forms import UserPasswordResetForm

urlpatterns = [
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path('password-reset',PasswordResetView.as_view(template_name ="password-reset-form.html", form_class = UserPasswordResetForm), name = "password-reset"),
    path('password-reset/done',PasswordResetDoneView.as_view(template_name ="password-reset-done.html"), name = "password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name ="password-reset-confirm.html"), name = "password_reset_confirm"),
    path('password-reset-complete',PasswordResetCompleteView.as_view(template_name ="password-reset-complete.html"), name = "password_reset_complete"),
]