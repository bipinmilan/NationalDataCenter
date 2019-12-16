from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from Federal.models import Executive


# @login_required
def private_data(request):
    if request.user.is_superuser or request.user.groups.filter(name="Federal_Executive").exists():
        private_data = Executive.objects.filter(is_private=True, is_published=True)
        context = {
            'private_data': private_data
        }
        return render(request, 'private/private_list.html', context)
    else:
        return HttpResponse('You are neither super admin & also do not belongs to related group')


def public_data(request):
    public_data = Executive.objects.filter(is_private=False)
    context = {
        'public_data': public_data
    }
    return render(request, 'public/public_list.html', context)
