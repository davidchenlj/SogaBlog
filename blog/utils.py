# -*- coding: utf-8 -*-
import os
from blog.libs.backstage.models import category

class Dict(dict):
    def __missing__(self, key):
        rv = self[key] = type(self)()
        return rv

def category_list(_key='response'):
    queryset=category.objects.all()
    f_arr=[]
    row_data=Dict()
    row_pid={}
    for row in queryset:
        row_data[row.id]['pid']=row.pid
        row_data[row.id]['name']=row.name
        row_data[row.id]['css']=row.css
        row_data[row.id]['display']=row.display
        row_data[row.id]['id']=row.id
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
        if _key == 'response':
            res.setdefault(_key, []).append(row_data[pid])
        else:
            res.setdefault(pid, []).append(row_data[pid])
    return res

def category_pid():
    queryset=category.objects.filter(pid=0)
    row_data=Dict()
    for row in queryset:
        row_data[row.id]['pid']=row.pid
        row_data[row.id]['name']=row.name
        row_data[row.id]['css']=row.css
        row_data[row.id]['display']=row.display
        row_data[row.id]['id']=row.id
    return row_data


def save_file(path, file_name, data):
    ''' 上传图片文件 '''
    if data == None:
        return

    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)

    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()