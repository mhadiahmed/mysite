"""
this site created by "Mhadi Ahmed" 
to contact me:
my Email : mahadyahmed@yahoo.com
my Facebook: https://www.facebook.com/brmag.sd
Facebook gruop: https://www.facebook.com/groups/sudanpython
my blog: http://brmmaga.blogspot.com/ 

this is the admin for register the model i have register one model name = Post in line 16

"""
from django.contrib import admin
from .models import Post


admin.site.register(Post)