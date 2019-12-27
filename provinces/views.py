from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, UpdateView, DeleteView

from provinces.forms import ProExecutiveForm
from provinces.models import ProvinceExecutive


class ProExecutiveListView(ListView):
    model = ProvinceExecutive
    template_name = 'cdb/provinces/executive/executive_data_list.html'
    context_object_name = 'executive_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def pro_upload(request):
    upload = ProExecutiveForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            upload = ProExecutiveForm(request.POST, request.FILES)
            if upload.is_valid():
                form = upload.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('pro-add-executive')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('pro-add-executive')

        else:
            return render(request, 'cdb/provinces/executive/add_executive_data.html', {'upload_pro': upload})
    else:
        return redirect('entry-login')


class ProExecutiveUpdateView(UpdateView):
    model = ProvinceExecutive
    template_name = 'cdb/provinces/executive/executive_update.html'
    context_object_name = 'executive_table'
    fields = ('title', 'description', 'category', 'related_file', 'is_private', 'is_published', 'related_ministry')

    def get_success_url(self):
        return reverse_lazy('pro-executive-data')


class ProExecutiveDelete(DeleteView):
    model = ProvinceExecutive
    template_name = 'cdb/partials/_pro-delete.html'
    context_object_name = 'executive_table'

    def get_success_url(self):
        return reverse_lazy('pro-executive-data')
