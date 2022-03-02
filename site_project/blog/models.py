from distutils.command.upload import upload
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
   
class Course(models.Model):
    name=models.CharField(max_length=200)
    tag=models.ManyToManyField(Tag,blank=True,null=True)
    students=models.ManyToManyField(User,blank=True,related_name='courses_joined')
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/")
    date=models.DateTimeField(auto_now=True)
    avaliable=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/")
    facebook=models.URLField(max_length=100,blank=True)
    instagram=models.URLField(max_length=100,blank=True)
    twitter=models.URLField(max_length=100,blank=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField(blank=True)
    def __str__(self):
        return self.email


