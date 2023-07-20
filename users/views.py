

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')