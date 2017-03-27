# -*- coding: utf-8 -*-
# Create your views here.
import os, sys, commands, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from blog.libs.backstage.models import category, article
from blog.libs.backstage.forms import categoryForm, articleForm
from blog.data_list import get_datatables_records
from django.shortcuts import redirect
from django.db.models import Q
from blog.utils import category_list, category_pid
from django.views import generic
from blog.libs.backstage.models import category, article
from django.views.generic import View

class IndexView(View):
    search_fields = []
    template_name="blog/blog_show.html"

    def get(self, request, pk):
        queryset = article.objects.get(pk=pk)
        article.objects.filter(pk=pk).update(browse=queryset.browse + 1)
        _category = category.objects.exclude(pid=0)
        return render(request, self.template_name, {
            "queryset": queryset,
            "category": _category
        })

    def post(self, request):
    	pass

class AuthorPostsView(generic.ListView):
    queryset=category.objects.all()
    template_name="blog/test.html"

    def get(self, request, *args, **kwargs):
    	print 'get'
    	return super(AuthorPostsView, self).get(
    		request, *args, **kwargs
    	)

    def dispatch(self, request, *args, **kwargs):
        self.xx=123
        print kwargs
        return super(AuthorPostsView, self).dispatch(
		    request, *args, **kwargs
		)

    def get_context_data(self, **kwargs):
        print 'get_context_data'
        context_data = super(AuthorPostsView, self).get_context_data(**kwargs)
        context_data['author'] = '111'
        context_data['dispatch'] = self.xx
        context_data['queryset'] = self.queryset
        return context_data
