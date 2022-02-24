from django.db import models
from django.forms import CharField

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True,null=True)
def __str__(self):
    return self.name

class Course(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/")
    date=models.DateTimeField(auto_now=True)
    avaliable=models.BooleanField(default=True)

def __str__(self):
    return self.name