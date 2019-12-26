from django.urls import path, include

from accounts.forms import EmailValidationOnForgotPassword
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .tokens import user_tokenizer

urlpatterns = [
    path('entry-login', views.data_entry_login, name='entry-login'),
    path('logout', views.logout, name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('msg/', views.msg, name='msg'),
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='cdb/accounts/reset_password.html',
            html_email_template_name='cdb/accounts/reset_password_email.html',
            success_url=settings.LOGIN_URL,
            form_class=EmailValidationOnForgotPassword,
            token_generator=user_tokenizer),
        name='reset_password'
    ),
    path(
        'reset-password-confirmation/<str:uidb64>/<str:token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='cdb/accounts/reset_password_update.html',
            post_reset_login=True,
            post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
            token_generator=user_tokenizer,
            success_url=settings.LOGIN_REDIRECT_URL),
        name='password_reset_confirm'
    ),
]
