from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from taskapp.forms import CommentForm, CreateupdateTaskForm
from taskapp.mixins import UserIsOwnerMixin
from taskapp.models import Comment, Task
from django.contrib.auth.forms import UserCreationForm
class TaskListView(ListView):
    model = Task
    template_name = "taskapp/tasks_list.html"
    context_object_name = "all_tasks"
    

class TaskDetailView(DetailView):
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    def post(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:

            form = CommentForm(request.POST, request.FILES)
            print("-------------")
            print(request.FILES)
            print("-------------")
            if form.is_valid():
                new_comment: Comment = form.instance
                new_comment.task = self.get_object()
                new_comment.user = self.request.user
                new_comment.save()
        
            return redirect(request.path_info)
        else:
            return HttpResponse("Try to login or register", status=403)


class TaskCreateForm(CreateView, LoginRequiredMixin):
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

class TaskDeleteView(UserIsOwnerMixin,DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/sign_in.html"
    success_url = reverse_lazy("task-list")

class CommentCreateForm(CreateView, UserIsOwnerMixin):
    model = Comment
    form_class = CommentForm
    template_name = "taskapp/comment_create.html"
    success_url = reverse_lazy("task-detail")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        

        return super().form_valid(form)
class CommentDeleteView(DeleteView, UserIsOwnerMixin):
    model = Comment
    success_url = reverse_lazy("task-detail")
class CommentEditView(UpdateView, UserIsOwnerMixin):
    model = Comment
    form_class = CommentForm
    template_name = "taskapp/comment_edit.html"
    success_url = reverse_lazy("task-detail")