from django import forms

from taskapp.models import Comment, Task

class CreateupdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["user"]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", "comment_pics")