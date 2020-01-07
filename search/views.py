from django.shortcuts import render

# Create your views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from Federal.models import Executive
from django.db.models import Q

'''class HomeView(TemplateView):
    template_name = 'search_page/search_result.html'''


class HomeView(TemplateView):
    template_name = 'search_page/home.html'


'''class FederalListView(ListView):
    template_name = 'search_page/search_result.html'
    model = Executive
    queryset = Executive.objects.all()
    context_object_name = 'executive'''


def search(request):
    queryset_list = Executive.objects.order_by('-title')
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            queryset_list = queryset_list.filter(Q(title__icontains=q) |
                                                 Q(related_ministry__name__icontains=q) |
                                                 Q(description__icontains=q)).distinct()

    context = {
        'items': queryset_list
    }
    return render(request, 'search_page/search_result.html', context)
