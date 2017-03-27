# -*- coding: utf-8 -*-
import time
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext,loader
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
         try:
             return dict.__getitem__(self, item)
         except KeyError:
             value = self[item] = type(self)()
             return value

def Search(queryset, request, search_fields):
    ''' 根据search_fields来查询 '''
    SearchKey = request.GET.get('search')
    outputQ = None
    kwargs = {}
    for t_field in search_fields:
        keywords = request.GET.get(t_field)
        if keywords:
            kwargs[t_field] = keywords
        if SearchKey:
            kwargz = {t_field + "__icontains": SearchKey}
            outputQ = outputQ | Q(**kwargz) if outputQ else Q(**kwargz)

    if len(kwargs) >= 1:
        return queryset.filter( **kwargs )
    elif outputQ:
        return queryset.filter(outputQ).distinct()
    else:
        return queryset

def get_datatables_utils(request, queryset, search_fields, template_name, extra_context={}):
    '''
     该函数实现了分页功能!
     queryset 一个Sql对象
     template_name 模板文件
     extra_context 包含参数等信息
    '''
    after_range_num = 5
    bevor_range_num = 4

    input_order=request.GET.get("inputOrder", 'null')
    _input_order='null'
    if input_order != 'null':
        _order=input_order.split('|')
        if _order[1] == "desc":
            queryset_desc=queryset.order_by(_order[0])
        elif _order[1] == "asc":
            queryset_desc=queryset.order_by('-%s' % _order[0])
        else:
            queryset_desc=queryset
        _input_order=_order[1]
    else:
        queryset_desc=queryset

    _queryset = Search(queryset_desc, request, search_fields)

    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    if extra_context.has_key('pagesize'):
        pagesize=extra_context['pagesize']
    else:
        pagesize=20
    pagesize = request.GET.get('pagesize', pagesize)
    paginator = Paginator(_queryset, int(pagesize))

    try:
        object_result = paginator.page(page)
    except:
        object_result = paginator.page(1)

    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+bevor_range_num]

    context = {
        'object_result':object_result,
        'request':request,
        'queryset':_queryset,
        'page_range':page_range,
        'pagesize':pagesize,
        'page':page,
        'input_orders':_input_order,
    }
    return context
