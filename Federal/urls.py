from Federal.views import public_data
from . import views
from django.urls import path

urlpatterns = [
    path('pd', views.private_data, name='private_data'),
    path('pb', public_data.as_view(), name='public_data'),
    path('upload', views.upload, name='upload'),
    path('entry-dashboard', views.index, name='entry-dashboard'),
]
