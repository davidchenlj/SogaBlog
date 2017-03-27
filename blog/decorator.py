# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from functools import wraps

def login_required():
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
             print request.user
             if not request.user.username:
                 return HttpResponseRedirect('/user/login/')
             return func(request, *args, **kwargs)
        return wraps(func)(inner_decorator)
    return decorator

class AdminOnlyMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.username:
            return HttpResponseRedirect('/user/login/')
        return super(AdminOnlyMixin, self).dispatch(request, *args, **kwargs)