# -*- coding: utf-8 -*-
import re, time,sys
from django import template
from random import choice
from blog.libs.backstage.models import category
register = template.Library()

reload(sys)
sys.setdefaultencoding('utf-8')

@register.filter
def show_category(pk):
    return category.objects.filter(pid=pk)

@register.filter
def time_change_stime(t):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(t)))

@register.filter
def tag_input(tag):
    input_txt=''
    for row in tag.split(','):
        input_txt=input_txt + '<input type="text" name="tag" value="{}">'.format(row)
    return input_txt

@register.filter
def tag_list(tag):
    input_txt=''
    for row in tag.split(','):
        input_txt=input_txt + '<a href="javascript:void(0)" name="span_tag" class="label label-success">{}</a>'.format(row)
    return input_txt

@register.filter
def index_tag(tag):
    input_txt=''
    for row in tag.split(','):
        input_txt=input_txt + '<a  href="/blog/index/?search={}" class="btn btn-default btn-xs tag_a">{}</a>&nbsp;&nbsp;'.format(row, row)
    return input_txt

@register.filter
def keyvalue(dict, key):
    if dict.has_key(key):
        if dict[key]['css']:
            html='<a class="post-category post-category-{}" href="#">{}</a>'.format(dict[key]['css'], dict[key]['name'])
            return html
    html='<a class="post-category" href="#">{}</a>'.format(dict[key]['name'])
    return html

@register.filter
def tag_style(v):
    stp = [
        'font-size: 12px; color: #ccc',
        'font-size: 15px; color: #ccc',
        'font-size: 19.5px; color: #7e7e7e',
        'font-size: 18px; color: #8e8e8e',
        'font-size: 28.5px; color: #212121',
        'font-size: 16.5px; color: #9d9d9d',
        'font-size: 16.5px; color: #9d9d9d',
        'font-size: 16.5px; color: #9d9d9d',
        'font-size: 27px; color: #303030'
    ]
    return choice(stp)
