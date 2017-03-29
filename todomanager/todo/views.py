from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from todo.models import Task
from django.views.generic import DetailView
from django.views.generic import CreateView
from todo.forms import TaskCreateForm
from todo.forms import TaskUpdateForm
from todo.forms import TaskDeleteForm
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class TaskListView(ListView):
    """Documentation de notre controleur."""
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks-list.html"
    paginate_by = None

class TaskRetrieveView(DetailView):
    """Doc"""
    model = Task
    context_object_name = "task"
    template_name = 'todo/task-detail.html'

class TaskCreateView(CreateView):
    """Doc"""
    model = Task
    form_class = TaskCreateForm
    template_name='todo/task-create.html'

    def get_initial(self):
        return{
            'created_by':self.request.user.member,
            'modified_by': self.request.user.member,
            'assigned_to': self.request.user.member
        }
class TaskUpdateView(UpdateView):
    model=Task
    form_class = TaskUpdateForm
    template_name='todo/task-create.html'
class TaskDeleteView(DeleteView):
    model=Task
    form_class=TaskDeleteForm
    template_name='todo/task-delete.html'
    success_url="/"