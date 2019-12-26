from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def data_entry_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.groups.filter(name='Data_Entry_Officer').exists():
            auth.login(request, user)
            return redirect('entry-dashboard')
        elif user is not None and user.is_superuser or user.groups.filter(
                name='Federal_Executive') or user.groups.filter(
            name='Federal_Judiciary') or user.groups.filter(name='Federal_Legislative').exists():
            auth.login(request, user)
            return redirect('/admin/login')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('entry-login')
    else:
        return render(request, 'cdb/accounts/data_entry_login.html')


@login_required(login_url='entry-login')
def logout(request):
    if request.method == 'POST' and request.user.groups.filter(name="Data_Entry_Officer").exists():
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('entry-login')


def msg(request):
    return render(request, 'cdb/accounts/send-msg.html')
