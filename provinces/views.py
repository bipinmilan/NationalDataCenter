from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, UpdateView, DeleteView

from provinces.forms import ProExecutiveForm
from provinces.models import ProvinceExecutive


class ExecutiveDataList(ListView):
    model = ProvinceExecutive
    template_name = 'cdb/federals/executive/executive_table_list.html'
    context_object_name = 'executive_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def upload(request):
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
                return redirect('add-executive-data')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('add-executive-data')

        else:
            return render(request, 'cdb/federals/executive/upload_form.html', {'upload_form': upload})
    else:
        return redirect('entry-login')


class ExecutiveUpdateView(UpdateView):
    model = ProvinceExecutive
    template_name = 'cdb/federals/executive/executive_update.html'
    context_object_name = 'executive_table'
    fields = ('title', 'description', 'category', 'related_file', 'is_private', 'is_published', 'related_ministry')

    def get_success_url(self):
        return reverse_lazy('executive-data')


class ExecutiveDelete(DeleteView):
    model = ProvinceExecutive
    template_name = 'cdb/partials/_delete.html'
    context_object_name = 'executive_table'

    def get_success_url(self):
        return reverse_lazy('executive-data')
