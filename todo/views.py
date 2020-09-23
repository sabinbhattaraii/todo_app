from django.shortcuts import render
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/home.html'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_new.html'
    fields = '__all__'

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/todo_edit.html'
    fields = '__all__'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('home')