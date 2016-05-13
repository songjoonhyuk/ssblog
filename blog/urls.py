from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^new/$', 'blog.views.post_new', name='post_new'),

]