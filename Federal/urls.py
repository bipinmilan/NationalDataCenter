from django.contrib.auth.decorators import login_required

from Federal.views import public_data, ExecutiveDataList
from . import views
from django.urls import path

urlpatterns = [
    path('pd', views.private_data, name='private_data'),
    path('pb', public_data.as_view(), name='public_data'),
    path('add-executive-data', views.upload, name='add-executive-data'),
    path('entry-dashboard', views.index, name='entry-dashboard'),
    # path('executive-data', views.retrieve_user_specific_data, name='executive-data'),
    path('executive-data', login_required(login_url='entry-login')(ExecutiveDataList.as_view()), name='executive-data')
    # path('<executive_id>', views.delete_executive_data, name='executive-delete'),
    # path('ex_update/<int:pk>', views.ExecutiveUpdate.as_view(), name='executive_update'),
    # path('ex_delete/<int:pk>', views.ExecutiveDelete.as_view(), name='executive_delete'),
    # path('delete/<int:id>', views.destroy),
]
