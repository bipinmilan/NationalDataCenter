from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, UpdateView
from Federal.forms import ExecutiveCreate
from Federal.models import Executive
from django.contrib import messages
from django.urls import reverse_lazy


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


@login_required(login_url='entry-login')
def index(request):
    return render(request, 'pages/index.html')


# class Table(ListView):
# template_name = 'federals/executive_table_list.html'
# queryset = Executive.objects.order_by('-timestamp').filter(is_published=True)
# context_object_name = 'executive_table'

# @login_required(login_url='entry-login')
'''def retrieve_user_specific_data(request):
    executive_table = Executive.objects.order_by('-timestamp').filter(author=request.user)
    context = {
        'executive_table': executive_table
    }
    return render(request, 'federals/executive_table_list.html', context)
'''


class ExecutiveDataList(ListView):
    model = Executive
    template_name = 'federals/executive_table_list.html'
    context_object_name = 'executive_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


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
                return redirect('add-executive-data')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('add-executive-data')

        else:
            return render(request, 'federals/upload_form.html', {'upload_form': upload})
    else:
        return redirect('entry-login')


'''def delete_executive_data(request, executive_id):
    executive_id = int(executive_id)
    executive_data = Executive.objects.get(pk=executive_id)
    executive_data.delete()
    return redirect('executive-data')'''

'''class ExecutiveUpdate(UpdateView):
    model = Executive
    fields = '__all__'
    success_url = reverse_lazy('executive-data')


class ExecutiveDelete(DeleteView):
    model = Executive
    success_url = reverse_lazy('executive-data')'''

'''def destroy(request, id):
    executive = Executive.objects.get(id=id)
    executive.delete()
    return redirect("executive-data")'''


class ExecutiveDelete(DeleteView):
    model = Executive
