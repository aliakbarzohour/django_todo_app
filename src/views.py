import datetime
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

# Create your views here.


def Home(request):
    context = Todo.objects.all()
    return render(request, 'home.html', {"Todos": context})

def Delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.error(request, ':( این بخش از کار ها حذف شد', 'danger')
    return redirect('home')

def Done(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, ' :) تبریک . این کار هم انجام شد', 'success')
    return redirect('home')
    