from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('courses',views.courses,name="courses"),
    path('courses/course_detail/<int:course_view_id>',views.course_detail,name="course_detail"),
    path('category/<int:category_view_id>', views.category_view, name='category_view'),
    path('tag/<int:tag_view_id>', views.tag_view, name='tag_view'),
    path('teachers',views.teachers_list,name="teachers"),
    path('teacher_detail/<int:teacher_view_id>',views.teacher_detail,name="teacher_detail"),
    path('contact',views.contact,name="contact"),
    path('login',views.user_login,name="login"),
    path('register',views.user_register,name="register"),
    path('dashboard',views.user_dashboard,name="dashboard"),
    path('logout',views.user_logout,name="logout"),
    path('enroll_the_course',views.enroll_the_course,name="enroll_the_course"),
]
