from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30)
    slug=models.SlugField()
    body=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)#auto add data for this column so that user doesnt input it.
    thumb=models.ImageField(default="",blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f'{self.title}'
    
    def snippet(self):
        return self.body[:50] + '...'
     