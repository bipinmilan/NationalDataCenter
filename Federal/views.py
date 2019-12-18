from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from Federal.forms import ExecutiveCreate
from Federal.models import Executive
from django.contrib import messages


# @login_required
def private_data(request):
    if request.user.is_superuser or request.user.groups.filter(name="Federal_Executive").exists():
        private_data = Executive.objects.filter(is_private=True, is_published=True)
        context = {
            'private_data': private_data
        }
        return render(request, 'private/private_list.html', context)
    else:
        return HttpResponse('You have not access to see private data')


class public_data(ListView):
    template_name = 'public/public_list.html'
    queryset = Executive.objects.filter(is_private=False)
    context_object_name = 'public_data'


def index(request):
    return render(request, 'pages/index.html')


def table(request):
    return render(request, 'entry_officer_admin_dashboard/executive_table_list.html')


def upload(request):
    upload = ExecutiveCreate()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            upload = ExecutiveCreate(request.POST, request.FILES)
            if upload.is_valid():
                form = upload.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('/upload')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('/upload')

        else:
            return render(request, 'entry_officer_admin_dashboard/upload_form.html', {'upload_form': upload})
    else:
        return redirect('entry-login')
