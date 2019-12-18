from django.urls import path

from . import views

urlpatterns = [
    path('entry-login', views.data_entry_login, name='entry-login'),
]
