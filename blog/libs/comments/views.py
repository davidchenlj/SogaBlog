# -*- coding: utf-8 -*-
# Create your views here.
import os, sys, commands, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from django.template.context_processors import csrf
from blog.libs.comments.models import discuss
from blog.data_list import get_datatables_records
from django.shortcuts import redirect
from django.db.models import Q

class Dict(dict):
    def __missing__(self, key):
        rv = self[key] = type(self)()
        return rv

def discuss_ajax(request, template_name):
    comment_id = request.POST.get('comment_id')
    queryset = discuss.objects.filter(comment_id=comment_id)
    if not queryset:
        return HttpResponse('not_comment')

    f_arr=[]
    row_data=Dict()
    row_pid={}
    for row in queryset:
        row_data[row.id]['id']=row.id
        row_data[row.id]['author']=row.author
        row_data[row.id]['author_email']=row.author_email
        row_data[row.id]['author_url']=row.author_url
        row_data[row.id]['pid']=row.pid
        row_data[row.id]['comment_id']=row.comment_id
        row_data[row.id]['comments']=row.comments
        row_data[row.id]['dateline']=row.dateline
        if row.pid == 0:
            f_arr.append(row.id)
        else:
            row_pid.setdefault(row.pid, []).append(row_data[row.id])
    res={}
    for pid in f_arr:
        row=Dict()
        if row_pid.has_key(pid):
            row_data[pid]['child']=row_pid[pid]
        else:
            row_data[pid]['child']=[]
        res.setdefault('response', []).append(row_data[pid])
    return render(request, template_name, {
        "res": res,
    })

def discuss_post(request):
    pid = request.REQUEST.get('pid')
    comments = request.REQUEST.get('comments')
    comment_id = request.REQUEST.get('comment_id')
    discuss.objects.create(comment_id=comment_id, author=u'老司机', author_email='49527444@qq.com', author_url='http://www.qq.com', dateline=int(time.time()), pid=pid, author_ip='192.168.1.1', comments=comments)
    return HttpResponse('ok')