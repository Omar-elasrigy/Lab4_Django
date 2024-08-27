from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate,logout
###################################################################################################

def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        elif 'register' in request.POST:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    else:
        login_form = AuthenticationForm()
        register_form = UserRegistrationForm()
    
    context = {
        'login_form': login_form,
        'register_form': register_form
    }
    
    return render(request, 'userAccounts/home.html', context)

###################################################################################################
def login_view(request):
    form = AuthenticationForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('list')  
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'userAccounts/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'userAccounts/register.html', {'form': form})  
