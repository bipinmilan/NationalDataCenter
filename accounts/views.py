from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def data_entry_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.groups.filter(name='Data_Entry_Officer').exists():
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('entry-dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('entry-login')
    else:
        return render(request, 'accounts/data_entry_login.html')


@login_required(login_url='entry-login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('entry-login')
