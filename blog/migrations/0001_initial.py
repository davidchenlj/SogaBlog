# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('img', models.CharField(max_length=100, null=True, verbose_name='\u7f29\u7565\u56fe', blank=True)),
                ('browse', models.IntegerField(default=0, null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f', blank=True)),
                ('dateline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('flag', models.IntegerField(default=b'1', null=True, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe6\x98\xbe\xe7\xa4\xba', blank=True)),
                ('access', models.IntegerField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe8\xae\xbe\xe7\xbd\xae', choices=[(1, '\u6240\u6709\u4eba'), (2, '\u81ea\u5df1')])),
                ('brief', models.TextField(null=True, verbose_name=b'\xe7\xae\x80\xe8\xa6\x81\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('detail', models.TextField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('tag', models.CharField(max_length=100, verbose_name='\u6807\u7b7e')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('pid', models.IntegerField(default=b'0', verbose_name='\u4e0a\u7ea7\u83dc\u5355ID')),
                ('css', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0', choices=[(b'design', '\u7eff\u8272'), (b'pure', '\u84dd\u8272'), (b'yui', '\u7d2b\u8272'), (b'js', '\u7ea2\u8272'), (b'ye', '\u9ec4\u8272'), (b'chengse', '\u6a59\u8272')])),
                ('display', models.IntegerField(default=b'1', verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba0\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba \xef\xbc\x8c1\xe6\x98\xbe\xe7\xa4\xba', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='discuss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.IntegerField(verbose_name='\u8bc4\u8bbaID')),
                ('author', models.CharField(max_length=100, null=True, verbose_name='\u8bc4\u8bba\u8005', blank=True)),
                ('author_email', models.CharField(max_length=100, null=True, verbose_name='\u8bc4\u8bba\u90ae\u7bb1', blank=True)),
                ('author_url', models.CharField(max_length=100, null=True, verbose_name='\u8bc4\u8bba\u7f51\u7ad9', blank=True)),
                ('dateline', models.CharField(max_length=100, null=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4', blank=True)),
                ('pid', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5b50\u8bc4\u8bba')),
                ('author_ip', models.CharField(max_length=100, null=True, verbose_name='\u8bc4\u8bba\u8005IP', blank=True)),
                ('comments', models.TextField(null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='pid',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='blog.category'),
        ),
    ]
