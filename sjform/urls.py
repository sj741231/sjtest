#coding=utf-8
from django.conf.urls import url
from sjform import views

urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^record-form/$', views.record_form),
    url(r'^record/$', views.record),
    url(r'^thanks/$', views.thanks),
    
]