"""
this site created by "Mhadi Ahmed" 
to contact me:
my Email : mahadyahmed@yahoo.com
my Facebook: https://www.facebook.com/brmag.sd
Facebook gruop: https://www.facebook.com/groups/sudanpython
my blog: http://brmmaga.blogspot.com/ 

this is the url file have 3 url(home page,contact,post+ the Named groups)

"""
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Post


urlpatterns=[
    url(r'^$', views.index),
    url(r'^contact/$', views.contact),
    url(r'^post/',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                              template_name="blog/post.html")),
    url(r'(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name=("blog/detail.html")))
]