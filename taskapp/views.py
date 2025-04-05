from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView

from taskapp.forms import CreateupdateTaskForm
from taskapp.mixins import UserIsOwnerMixin
from taskapp.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "taskapp/tasks_list.html"
    context_object_name = "all_tasks"
    

class TaskDetailView(DetailView):
    model = Task

class TaskCreateForm(CreateView):
    model = Task
    form_class = CreateupdateTaskForm
    template_name = "taskapp/task_create.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        

        return super().form_valid(form)
    
class TaskEditView(UpdateView, UserIsOwnerMixin):
    model = Task
    form_class = CreateupdateTaskForm
    template_name = "taskapp/task_create.html"
    success_url = reverse_lazy("task-list")