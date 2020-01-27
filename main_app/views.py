from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo

class TodoCreate(CreateView):
  model = Todo
  fields = '__all__'
  success_url = '/todos/'
class TodoUpdate(UpdateView):
  model = Todo
  fields = ['name', 'description', 'number']
  success_url = '/todos/'
class TodoDelete(DeleteView):
  model = Todo
  fields = '__all__'
  success_url = '/todos/'


#TODOS
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def todos_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', { 'todos': todos })
def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html', { 'todo': todo })

