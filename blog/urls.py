from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from blog.libs.backstage.models import category, article
from blog.libs.index.views import BlogView, BlogDetail
from blog.libs.backstage.views import CategoryUpdateView, CategoryCreateView, ArticleUpdateView,\
     ArticleCreateView, ArticleView, CategoryView

urlpatterns = patterns('blog.libs.backstage.views',
      url(r'^login/$', 'Login', {'template_name': 'backstage/login.html'}, name='login'),
      url(r'^del_category/$', 'del_category', name='del_category'),
      url(r'^del_article/$', 'del_article', name='del_article'),
      url(r'^uploadImg/$', 'uploadImg', name='uploadImg'),
)

urlpatterns += patterns('blog.libs.index.views',
      url(r'^archive/$', 'archive', {'template_name': 'blog/archive.html'}, name='archive'),
      url(r'^about/$', 'about', {'template_name': 'blog/about.html'}, name='about'),
)

urlpatterns += patterns('blog.libs.comments.views',
      url(r'^discuss_ajax/$', 'discuss_ajax', {'template_name': 'base/comment.html'},  name='discuss_ajax'),
      url(r'^discuss_post/$', 'discuss_post', name='discuss_post'),
)

urlpatterns += [
        url(r'^index/$', BlogView.as_view(), name='blog_index'),
        url(r'^show/(?P<pk>\d+)/$', BlogDetail.as_view(), name='blog_show'),
        url(r'^category_edit/(?P<pk>\d+)/$', CategoryUpdateView.as_view(), name='category_edit'),
        url(r'^category_add/$', CategoryCreateView.as_view(), name='category_add'),
        url(r'^article_edit/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='article_edit'),
        url(r'^blog_add/$', ArticleCreateView.as_view(), name='blog_add'),
        url(r'^article_list/$', ArticleView.as_view(), name='article_list'),
        url(r'^category/$', CategoryView.as_view(), name='category_index'),
        
        
        
]
