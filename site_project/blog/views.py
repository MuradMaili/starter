
from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate,login,logout
from . models import Category, Course,Tag, Teacher
from . forms import ContactFrom
from . formslogin import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




def index(request):
    context={
        "total_course":Course.objects.all().count()
    }
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")

def courses(request):
    categories=Category.objects.all()
    tag=Tag.objects.all()
    context={
        "courses":Course.objects.all().order_by('-date'),
        "categories":categories,
        'tag':tag
    }
    return render(request,"courses.html",context)
    

def course_detail(request,course_view_id):
    course=Course.objects.get(id=course_view_id)
    
    return render(request,"course.html",{
        "course":course
    })
def category_view(request,category_view_id):
    categories=Category.objects.all()
    tag=Tag.objects.all()
    courses=Course.objects.all().filter(category=category_view_id)
    return render(request,"courses.html",{
        "courses":courses,  
        "categories":categories,
        'tag':tag
    })
def tag_view(request,tag_view_id):
    categories=Category.objects.all()
    tag=Tag.objects.all()
    courses=Course.objects.all().filter(tag=tag_view_id)
    return render(request,"courses.html",{
        "courses":courses,  
        "categories":categories,
        'tag':tag
    })
def teachers_list(request):
    teachers=Teacher.objects.all()
    context={
        "teachers":teachers
    }
    return render(request,"teachers.html",context)

def teacher_detail(request,teacher_view_id):
    teacher=Teacher.objects.get(id=teacher_view_id)
    
    return render(request,"teachers_detail.html",{
        "teacher":teacher
    })

def contact(request):
    
    form=ContactFrom(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,"updated successfuly")
            return HttpResponsePermanentRedirect(reverse("contact"))
    context = {
        "form": form
    }
    return render(request, "contact.html", context)

def user_login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return render(request,"login.html",{
                "error":"username or password wrong"
            })
    return render(request,"login.html")  
    
    
def user_register(request):
    
    if request.method == 'POST':
        #Get from values
        firstname =  request.POST['firstname']
        lastname =  request.POST['lastname']
        username =  request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        password2 =  request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, 
                    email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    courses=current_user.courses_joined.all() #Course modelinde courses_joined e gedir
    context={
        'courses':courses
    }
    return render(request,"dashboard.html",context)
def user_logout(request):
    logout(request)
    return redirect('index')

def enroll_the_course(request):
    course_id = request.POST['course_id']
    user_id=request.POST['user_id']
    if request.user.is_authenticated:
         course=Course.objects.get(id=course_id)
         user=User.objects.get(id=user_id)
         course.students.add(user)
         return redirect('dashboard')
    else:
         return redirect("login")
    

