from django.urls import path

from . import views

urlpatterns = [
    path("task/list/", views.TaskListView.as_view(), name="task-list"),
    path("task/detail/<int:pk>", views.TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", views.TaskCreateForm.as_view(), name="task-create"),
    path("task/edit/<int:pk>", views.TaskEditView.as_view(), name="task-edit"),
]