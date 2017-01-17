"""
this site created by "Mhadi Ahmed" 
to contact me:
my Email : mahadyahmed@yahoo.com
my Facebook: https://www.facebook.com/brmag.sd
Facebook gruop: https://www.facebook.com/groups/sudanpython
my blog: http://brmmaga.blogspot.com/ 

this is the model file have 1 model Post(title,contact,date)
and 2 definition for unicode the text 
one for python 3 : __str__
one for python 2 : __unicode__

"""
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField(default=' ') 
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)
    
    def __unicode__(self):
        return str(self.title)
