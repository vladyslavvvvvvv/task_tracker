from django import forms

from taskapp.models import Task

class CreateupdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["user"]