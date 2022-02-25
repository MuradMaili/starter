from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('courses',views.courses,name="courses"),
    path('<slug:category_slug>/<int:course_id>',views.course_detail,name="course_detail"),
]
