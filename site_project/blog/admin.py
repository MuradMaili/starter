from django.contrib import admin
from . models import Category, Contact, Course,Tag,Teacher


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Teacher)
admin.site.register(Contact)
