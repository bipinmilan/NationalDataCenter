from django.urls import path
from search import views
from search.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('data', FederalListView.as_view(), name='data')
    path('search/', views.search, name='search')
]
