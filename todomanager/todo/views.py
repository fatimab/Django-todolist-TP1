from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from todo.models import Task


class TaskListView(ListView):
    """Documentation de notre controleur."""
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks-list.html"
    paginate_by = None

						