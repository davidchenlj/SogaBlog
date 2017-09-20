# -*- coding: utf-8 -*-
import os, sys, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from blog.libs.backstage.models import category, article
from blog.libs.backstage.forms import categoryForm, articleForm
from blog.data_list import get_datatables_records
from blog.data_list_utils import get_datatables_utils
from blog.utils import category_list, category_pid
from django.views import generic

class BlogView(generic.ListView):
    template_name="blog/blog_index.html"
    category_pid=category_pid()
    category_child = category.objects.exclude(pid=0)
    search_fields = ['pid__name', 'title', 'tag']
    
    def get_queryset(self):
        if self.request.user.username:
            queryset = article.objects.all().order_by('-id')
        else:
            queryset = article.objects.filter(access=1).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super(BlogView, self).get_context_data(**kwargs)
        context_data['category'] = self.category_child
        context_data['category_pid'] = self.category_pid
        context_data['category_count'] = self.category_child.count()
        context_data['queryset_count'] = self.get_queryset().count()
        context_data['pagesize'] = 10
        context=get_datatables_utils(
                self.request,
                self.get_queryset(),
                self.search_fields,
                self.template_name,
                extra_context={}
                )
        context_data.update(context)
        return context_data


class BlogDetail(generic.DetailView):
    model = article
    category_pid = category.objects.exclude(pid=0)
    template_name = 'blog/blog_show.html'

    def get_context_data(self, *args, **kwargs):
        obj = self.get_object()
        article.objects.filter(pk=obj.pk).update(browse=obj.browse+1)
        context_data = super(BlogDetail, self).get_context_data(*args, **kwargs)
        context_data['category'] = self.category_pid
        return context_data

def archive(request, template_name):
    '''  归档 '''
    return render(request, template_name, {'content':'没啥内容,先不归档...'})

def tag(request, template_name):
    '''  归档 '''
    queryset=article.objects.all()
    _TAG=[]
    for row in queryset:
        for _tag in row.tag.split(','): _TAG.append(_tag)
    _TAG_LIST=set(list(_TAG))
    return render(request, template_name, {'content':'没啥内容,先不归档...', 'TAG_LIST' : _TAG_LIST})

def about(request, template_name):
    ''' 关于 '''
    return render(request, template_name, {'content':'作者毕业于蓝翔高级技工学校已经学会了会用电脑操控挖掘机炒菜...'})