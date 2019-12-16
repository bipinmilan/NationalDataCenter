from . import views
from django.urls import path

urlpatterns = [
    path('pd', views.private_data, name='private_data'),
    path('pb', views.public_data, name='public_data'),
]
