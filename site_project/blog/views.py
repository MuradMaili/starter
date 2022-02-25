from django.shortcuts import render
from . models import Course


def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def courses(request):
    context={
        "courses":Course.objects.all().order_by('-date')

    }
    return render(request,"courses.html",context)

def course_detail(request,category_slug,course_id):
    course=Course.objects.get(category__slug=category_slug,id = course_id)
    return render(request,"course.html",{
        "course":course
    })