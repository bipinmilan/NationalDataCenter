from django.contrib.auth.decorators import login_required

from Federal.views import public_data, ExecutiveDataList, ExecutiveUpdateView, ExecutiveDelete, JudiciaryDataList, \
    JudiciaryUpdateView, JudiciaryDelete, LegislativeDataList, LegislativeUpdateView, LegislativeDelete
from . import views
from django.urls import path

urlpatterns = [
    path('pd', views.public_data, name='public_data'),
    # path('pb', public_data.as_view(), name='public_data'),
    path('add-executive-data', views.upload, name='add-executive-data'),
    path('entry-dashboard', views.index, name='entry-dashboard'),
    path('executive-data', login_required(login_url='entry-login')(ExecutiveDataList.as_view()), name='executive-data'),
    path('executive_table/<int:pk>/update', login_required(login_url='entry-login')(ExecutiveUpdateView.as_view()),
         name='executive-update'),
    path('executive_table/<int:pk>/delete', login_required(login_url='entry-login')(ExecutiveDelete.as_view()),
         name='executive-delete'),
    # Judiciary URL configuration
    path('judiciary-data', login_required(login_url='entry-login')(JudiciaryDataList.as_view()), name='judiciary-data'),
    path('add-judiciary-data', views.add_judiciary, name='add-judiciary-data'),

    path('judiciary_table/<int:pk>/update', login_required(login_url='entry-login')(JudiciaryUpdateView.as_view()),
         name='judiciary-update'),

    path('judiciary_table/<int:pk>/delete', login_required(login_url='entry-login')(JudiciaryDelete.as_view()),
         name='judiciary-delete'),

    # Legislative URL configuration
    path('legislative-data', login_required(login_url='entry-login')(LegislativeDataList.as_view()),
         name='legislative-data'),
    path('add-legislative-data', views.add_legislative, name='add-legislative-data'),

    path('legislative_table/<int:pk>/update', login_required(login_url='entry-login')(LegislativeUpdateView.as_view()),
         name='legislative-update'),

    path('legislative_table/<int:pk>/delete', login_required(login_url='entry-login')(LegislativeDelete.as_view()),
         name='legislative-delete'),
]
