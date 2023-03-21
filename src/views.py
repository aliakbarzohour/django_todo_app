from django.shortcuts import render
from .models import Todo

# Create your views here.


def Home(request):
    context = Todo.objects.all()
    return render(request, 'home.html', {"Todos": context})
