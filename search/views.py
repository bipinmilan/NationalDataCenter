from django.shortcuts import render

# Create your views
from django.views.generic import TemplateView, ListView

from Federal.models import Executive

'''class HomeView(TemplateView):
    template_name = 'search_page/search_result.html'''


class FederalListView(ListView):
    template_name = 'search_page/search_result.html'
    model = Executive
    queryset = Executive.objects.all()
    context_object_name = 'executive'
