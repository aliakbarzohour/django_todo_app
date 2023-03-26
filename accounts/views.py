from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
                    cd = form.cleaned_data
                    User.objects.create_user(cd['username'], cd['email'], cd['password'])
                    messages.success(request, 'تبریک . شما با موفقیت ثبت نام شدید', 'success')
                    return redirect('login ')


    else:
        form = UserRegistrationForm()
    return render(request , 'register.html', {'form':form})

def user_login(request):
      if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data      
            
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'تبریک . شما با موفقیت وارد شدید', 'success')
                return redirect('home')
      else:
            form = UserLoginForm
            return render(request, 'login.html', {'form':form}) 
      

def user_logout(request):
    logout(request)
    messages.success(request, 'شما از حساب کاربری خود خارج شدید', 'warning')
    return redirect('home')
