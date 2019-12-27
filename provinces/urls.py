from django.contrib.auth.decorators import login_required

from provinces import views
from django.urls import path

from provinces.views import ProExecutiveListView, ProExecutiveUpdateView, ProExecutiveDelete

urlpatterns = [
    path('pro-add-executive', views.pro_upload, name='pro-add-executive'),
    path('pro-executive-data', login_required(login_url='entry-login')(ProExecutiveListView.as_view()),
         name='pro-executive-data'),
    path('executive/<int:pk>/update', login_required(login_url='entry-login')(ProExecutiveUpdateView.as_view()),
         name='executive-update'),
    path('executive/<int:pk>/delete', login_required(login_url='entry-login')(ProExecutiveDelete.as_view()),
         name='executive-delete'),

]
