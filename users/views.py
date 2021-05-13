from django.shortcuts import render, redirect
from .forms import RegistrationForm, DeleteForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog_home')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'users/register_account.html', context)


def delete(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        username = request.POST.get('username')

        if username == request.user.username:
            user = request.user
            user.delete()
            return redirect('blog_home')
    else:
        form = DeleteForm()

    context = {'form': form}

    return render(request, 'users/delete_account.html', context)
