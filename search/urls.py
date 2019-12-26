from django.urls import path

from search.views import FederalListView

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', FederalListView.as_view(), name='executive')
]
