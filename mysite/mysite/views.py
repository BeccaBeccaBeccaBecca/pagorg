from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')
