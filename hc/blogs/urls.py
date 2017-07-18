from django.conf.urls import url
from hc.blogs import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^view/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),
    url(r'^category/(?P<slug>[-^\.]+).html',  views.view_categories, name='view_blog_category'),
    url(r'^new_post/$', views.new_post, name='new_post')
    ]
