from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def index(request):
    return render(request, 'band/index.html')

def about(request):
    return render(request, 'band/about.html')

def music(request):
    return render(request, 'band/music.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('band:index')
    else:
        form = RegistrationForm()
    return render(request, 'band/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Fixed: Use AuthenticationForm for login
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('band:index')
    else:
        form = AuthenticationForm()
    return render(request, 'band/login.html', {'form': form})

def user_logout(request):
    auth_logout(request)  # Fixed: Proper logout implementation
    return redirect('band:index')
