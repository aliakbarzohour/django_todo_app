import datetime
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import CreateTodo, EditTodo

# Create your views here.


def Home(request):
    context = Todo.objects.all()
    return render(request, 'home.html', {"Todos": context})

def Delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.error(request, 'این بخش از کار ها حذف شد  :( ', 'danger')
    return redirect('home')

def Done(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, ' تبریک . این کار هم انجام شد  :) ', 'success')
    return redirect('home')
    

def Create(request):
    if request.method == "POST":
        form = CreateTodo(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], sub_title=cd['sub_title'], body=cd['body'], date=cd['date'])
            if cd['date'] == '':
                datetime.now()
            messages.success(request, 'بخش جدید به لیست کار ها اضافه شد', 'success')
            return redirect('home')
    else:
        form = CreateTodo()
        
    return render(request, 'create.html', {'form':form})



def Edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = EditTodo(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'ویرایش با موفقیت انجام شد', 'success')
            return redirect('home')
    else:
        form = EditTodo(instance=todo)
        return render(request, 'edit.html', {'form':form})