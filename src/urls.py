from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('delete/<int:todo_id>/', views.Delete, name='delete'),
    path('done/<int:todo_id>/', views.Done, name='done'),
    path('create/', views.Create, name='create'),
    path('edit/<int:todo_id>/', views.Edit, name='edit'),
]
