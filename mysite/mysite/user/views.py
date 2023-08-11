# user/views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the homepage or login page after successful registration
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['username'] = user.username 
            if next_url:
                return redirect(next_url)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    # Redirect the user to the homepage or any other page after logout
    return redirect('home') 
