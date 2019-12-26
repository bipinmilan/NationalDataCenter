from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, UpdateView
from Federal.forms import ExecutiveCreate, JudiciaryForm, LegislativeForm
from Federal.models import Executive, Legislative, Judiciary
from django.contrib import messages
from django.urls import reverse_lazy


# @login_required
def public_data(request):
    if request.user.is_superuser or request.user.groups.filter(name="Federal_Executive").exists():
        private_data = Executive.objects.filter(is_private=False, is_published=True)
        context = {
            'private_data': private_data
        }
        return render(request, 'private/private_list.html', context)
    else:
        return HttpResponse('You have not access to see private data')


'''class public_data(ListView):
    template_name = 'public/public_list.html'
    queryset = Executive.objects.filter(is_private=False)
    context_object_name = 'public_data'''


@login_required(login_url='entry-login')
def index(request):
    return render(request, 'cdb/pages/index.html')


class ExecutiveDataList(ListView):
    model = Executive
    template_name = 'cdb/federals/executive/executive_table_list.html'
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
            return render(request, 'cdb/federals/executive/upload_form.html', {'upload_form': upload})
    else:
        return redirect('entry-login')


class ExecutiveUpdateView(UpdateView):
    model = Executive
    template_name = 'cdb/federals/executive/executive_update.html'
    context_object_name = 'executive_table'
    fields = ('title', 'description', 'category', 'related_file', 'is_private', 'is_published', 'related_ministry')

    def get_success_url(self):
        return reverse_lazy('executive-data')


class ExecutiveDelete(DeleteView):
    model = Executive
    template_name = 'cdb/partials/_delete.html'
    context_object_name = 'executive_table'

    def get_success_url(self):
        return reverse_lazy('executive-data')


# Judiciary CRUD
class JudiciaryDataList(ListView):
    model = Judiciary
    template_name = 'cdb/federals/judiciary/judiciary_table_list.html'
    context_object_name = 'judiciary_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def add_judiciary(request):
    add_jud = JudiciaryForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            add_jud = JudiciaryForm(request.POST, request.FILES)
            if add_jud.is_valid():
                form = add_jud.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('add-judiciary-data')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('add-judiciary-data')

        else:
            return render(request, 'cdb/federals/judiciary/judiciary_add_data.html', {'add_jud': add_jud})
    else:
        return redirect('entry-login')


class JudiciaryUpdateView(UpdateView):
    model = Judiciary
    template_name = 'cdb/federals/judiciary/judiciary_update.html'
    context_object_name = 'judiciary_table'
    fields = ('title', 'description', 'category', 'related_file', 'is_private', 'is_published', 'related_court')

    def get_success_url(self):
        return reverse_lazy('judiciary-update', kwargs={'pk': self.object.id})


class JudiciaryDelete(DeleteView):
    model = Judiciary
    template_name = 'cdb/federals/judiciary/_delete.html'
    context_object_name = 'judiciary_table'

    def get_success_url(self):
        return reverse_lazy('judiciary-data')


# Legislative CRUD
class LegislativeDataList(ListView):
    model = Legislative
    template_name = 'cdb/federals/legislative/legislative_table_list.html'
    context_object_name = 'legislative_table'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


def add_legislative(request):
    add_leg = LegislativeForm()
    if request.user.groups.filter(name="Data_Entry_Officer").exists():
        if request.method == 'POST':
            add_leg = LegislativeForm(request.POST, request.FILES)
            if add_leg.is_valid():
                form = add_leg.save(commit=False)
                form.author = request.user
                form.last_modified_by = request.user
                form.save()
                messages.success(request, 'Data Entered Successfully')
                return redirect('add-legislative-data')
            else:
                messages.error(request, 'Invalid Form Data!!')
                return redirect('add-legislative-data')

        else:
            return render(request, 'cdb/federals/legislative/legislative_add_data.html', {'add_leg': add_leg})
    else:
        return redirect('entry-login')


class LegislativeUpdateView(UpdateView):
    model = Legislative
    template_name = 'cdb/federals/legislative/legislative_update.html'
    context_object_name = 'legislative_table'
    fields = ('title', 'description', 'category', 'related_file', 'is_private', 'is_published', 'related_house')

    def get_success_url(self):
        return reverse_lazy('legislative-update', kwargs={'pk': self.object.id})


class LegislativeDelete(DeleteView):
    model = Legislative
    template_name = 'cdb/federals/legislative/_delete.html'
    context_object_name = 'legislative_table'

    def get_success_url(self):
        return reverse_lazy('legislative-data')

