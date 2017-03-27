# -*- coding: utf-8 -*-
import time
from django.db import models
import django.utils.timezone as timezone

class discuss(models.Model):
    comment_id = models.IntegerField(u'评论ID')
    author = models.CharField(u'评论者', max_length=100, null=True,blank=True)
    author_email = models.CharField(u'评论邮箱', max_length=100, null=True,blank=True)
    author_url = models.CharField(u'评论网站', max_length=100, null=True,blank=True)
    dateline = models.CharField(u'评论时间', max_length=100, null=True,blank=True)
    pid = models.IntegerField(u'是否子评论', default=0)
    author_ip = models.CharField(u'评论者IP', max_length=100, null=True,blank=True)
    comments = models.TextField('评论', null=True,blank=True)
    class Meta:
        app_label = 'blog'

    def __unicode__(self):
        return self.author_url