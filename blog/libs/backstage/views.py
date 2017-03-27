# -*- coding: utf-8 -*-
# Create your views here.
import os, sys, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.template.context_processors import csrf
from blog.libs.backstage.models import category, article
from blog.libs.backstage.forms import categoryForm, articleForm
from blog.data_list import get_datatables_records
from django.shortcuts import redirect
from blog.decorator import login_required, AdminOnlyMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView,\
    UpdateView, FormView, TemplateView, View
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from blog.utils import category_list
from blog.data_list_utils import get_datatables_utils

class CategoryUpdateView(AdminOnlyMixin, UpdateView):
    model = category
    template_name = "backstage/category_edit.html"
    form_class = categoryForm
    success_url = reverse_lazy('category_index')

    def get_context_data(self, **kwargs):
        context_data = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context_data['category'] = category.objects.filter(pid=0)
        return context_data

class CategoryCreateView(AdminOnlyMixin, CreateView):
    template_name = "backstage/category_add.html"
    form_class = categoryForm
    success_url = reverse_lazy('category_index')

    def get_context_data(self, **kwargs):
        context_data = super(CategoryCreateView, self).get_context_data(**kwargs)
        context_data['category'] = category.objects.filter(pid=0)
        return context_data


class CategoryView(AdminOnlyMixin, ListView):
    template_name="backstage/category_index.html"
    search_fields = ['username']


    def get_queryset(self):
        from blog.utils import category_list
        return category_list().copy()

    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data(**kwargs)
        context_data['First'] = category.objects.filter(pid=0)
        context_data['res'] = self.get_queryset().items()
        return context_data

class ArticleView(AdminOnlyMixin, ListView):
    template_name="backstage/article_list.html"
    search_fields = ['username']
    queryset = article.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super(ArticleView, self).get_context_data(**kwargs)
        context=get_datatables_utils(
                self.request,
                self.queryset,
                self.search_fields,
                self.template_name,
                extra_context={}
                )
        context_data.update(context)
        return context_data

class ArticleCreateView(AdminOnlyMixin, CreateView):
    form_class = articleForm
    model = article
    template_name = 'backstage/blog_add.html'
    success_url = reverse_lazy('category_index')

    def form_valid(self, form):
        self.tab = form.save(commit=False)
        tag_list=self.request.POST.getlist('tag', None)
        if tag_list:
            self.tab.tag=','.join(tag_list)
        self.tab.save()
        return redirect('article_list')

    def get_context_data(self, **kwargs):
        context_data = super(ArticleCreateView, self).get_context_data(**kwargs)
        context_data['category'] = category.objects.filter(pid=0)
        return context_data

class ArticleUpdateView(AdminOnlyMixin, UpdateView):
    form_class = articleForm
    model = article
    template_name = 'backstage/blog_add.html'
    success_url = reverse_lazy('category_index')

    def form_valid(self, form):
        self.tab = form.save(commit=False)
        tag_list=self.request.POST.getlist('tag', None)
        if tag_list:
            self.tab.tag=','.join(tag_list)
        self.tab.save()
        return redirect('article_list')

    def get_context_data(self, **kwargs):
        context_data = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context_data['category'] = category.objects.filter(pid=0)
        return context_data


@login_required()
def del_category(request):
    ''' 删除菜单'''
    pk = request.REQUEST.get('pk')
    tids = [int(i) for i in pk.split(',')]
    if len(tids) > 0:
        category.objects.filter(id__in=tids).delete()
    return redirect('category_index')

@login_required()
def del_article(request):
    ''' 删除文章'''
    pk = request.REQUEST.get('pk')
    tids = [int(i) for i in pk.split(',')]
    if len(tids) > 0:
        article.objects.filter(id__in=tids).delete()
    return redirect('article_list')

@login_required()
def uploadImg(request):
    ''' 上传图片接口 '''
    from blog.utils import save_file
    from SogaBlog import settings
    if request.method == 'POST':
        buf = request.FILES.get('imgFile', None)
        file_buff = buf.read()
        time_format = str(time.strftime("%Y-%m-%d-%H%M%S", time.localtime()))
        img_dir = os.path.join(settings.STATIC_PATH, 'blog_img')
        try:
            file_name = "img_" + time_format + ".jpg"
            save_file(img_dir, file_name, file_buff)
            dict_tmp = {}
            dict_tmp["error"] = 0
            dict_tmp["file_path"] = "/static/blog_img/" + file_name
            return HttpResponse(json.dumps(dict_tmp))
        except Exception, e:
            dict_tmp = {}
            dict_tmp["error"] = 1
            return HttpResponse(json.dumps(dict_tmp))

def Login(request, template_name):
    ''' 登录 '''
    from django.contrib.auth import authenticate, login, logout
    vt = loader.get_template(template_name)
    if request.POST:
        loguser = request.POST['username']
        logpass = request.POST['password']
        user = authenticate(username=loguser, password=logpass)
        if user is not None:
            login(request,user)
            return redirect('article_list')
        return redirect('login')
    c = RequestContext(request,{})
    return HttpResponse(vt.render(c))