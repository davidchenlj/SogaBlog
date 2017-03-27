from django.conf.urls import include, url
from django.contrib import admin
from blog.libs.index.views import BlogView

urlpatterns = [
    # Examples:
    # url(r'^$', 'SogaBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', BlogView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url('^blog/',include('blog.urls')),
]
