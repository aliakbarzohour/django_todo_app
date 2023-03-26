from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        pass
    else:
        form = UserRegistrationForm()
    return render(request , 'register.html', {'form':form})