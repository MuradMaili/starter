from django.shortcuts import render
from . models import Course
from django.utils.text import slugify

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def courses(request):
    context={
        "courses":Course.objects.all().order_by('-date')

    }
    return render(request,"courses.html",context)

def course_detail(request,slug):
    course=Course.objects.get(slug=slug)
    return render(request,"course.html",{
        "course":course
    })