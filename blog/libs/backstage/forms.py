# -*- coding: utf-8 -*-
import re
import datetime
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from blog.libs.backstage.models import category, article

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        exclude = ()

class articleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(articleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['style'] = 'width:300px'
        self.fields['brief'].widget.attrs['style'] = 'width:1000px; height:400px;'
        self.fields['detail'].widget.attrs['style'] = 'width:1000px; height:800px;'

    class Meta:
        model = article
        exclude = ()