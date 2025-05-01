from django import dispatch, forms
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from .models import Task
class UserIsOwnerMixin(object):
    def dispatch(self, request:HttpRequest, *args, **kwargs):
        instance:Task = self.get_object()
        if instance.user == request.user:
            return super().dispatch(request,*args, **kwargs )
        else:
            raise PermissionDenied
