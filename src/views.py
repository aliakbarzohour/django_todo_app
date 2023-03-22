import datetime
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def Home(request):
    context = Todo.objects.all()
    return render(request, 'home.html', {"Todos": context})

def Delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')

def Done(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')
    