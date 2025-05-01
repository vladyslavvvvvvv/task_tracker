from django.contrib import admin

from taskapp.models import Comment, Task

admin.site.register(Task)
admin.site.register(Comment)