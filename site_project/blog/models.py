from django.db import models
from django.forms import CharField
from django.utils.text import slugify

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True,null=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class Course(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/")
    date=models.DateTimeField(auto_now=True)
    avaliable=models.BooleanField(default=True)
    def __str__(self):
        return self.name

