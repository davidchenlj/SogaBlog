# -*- coding: utf-8 -*-
import time
from django.db import models
import django.utils.timezone as timezone

ACCESS_CHOICES = (
    (1, u'所有人'),
    (2, u'自己'),
)

CATEGORY_CSS_CHOICES = (
    ('design', u'绿色'),
    ('pure', u'蓝色'),
    ('yui', u'紫色'),
    ('js', u'红色'),
    ('ye', u'黄色'),
    ('chengse', u'橙色'),
)

class category(models.Model):
    name = models.CharField(u'分类名称', max_length=30)
    pid = models.IntegerField(u'上级菜单ID', default="0")
    css = models.CharField(u'分类名称', max_length=30, choices=CATEGORY_CSS_CHOICES)
    display = models.IntegerField('是否显示0不显示 ，1显示', default="1", blank=True)

    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.name

class article(models.Model):
    title = models.CharField(u'分类名称', max_length=30)
    img = models.CharField(u'缩略图', max_length=100, null=True,blank=True)
    browse = models.IntegerField('浏览量', default=0, null=True,blank=True)
    pid = models.ForeignKey(category, verbose_name='分类')
    dateline = models.DateTimeField(u'创建日期', default = timezone.now)
    flag = models.IntegerField('推荐显示', default="1", null=True,blank=True)
    access = models.IntegerField('权限设置', choices=ACCESS_CHOICES)
    brief = models.TextField('简要描述', null=True,blank=True)
    detail = models.TextField('详细描述', null=True,blank=True)
    tag = models.CharField(u'标签', max_length=100)
    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.title