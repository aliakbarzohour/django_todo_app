from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
                    cd = form.cleaned_data
                    User.objects.create_user(cd['username'], cd['email'], cd['password'])
                    messages.success(request, 'تبریک . شما با موفقیت ثبت نام شدید', 'success')
                    return redirect('home')


    else:
        form = UserRegistrationForm()
    return render(request , 'register.html', {'form':form})