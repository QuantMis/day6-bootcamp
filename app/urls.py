# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from authentication.views import *
from courses.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # courses page
    path('', login_view, name="login"),
    path('dashboard/courses/list', dashboard_courses_list, name="courses_list"),
    path('dashboard/courses/enrolled/list', dashboard_enrolled_courses_list, name="courses_list_enrolled"),
    path('dashboard/performance', dashboard_performance, name="performance"),
    path('enroll/<str:id>', enroll_course, name="enroll_course"),
    path('unenroll/<str:id>', unenroll_course, name="un_enroll_course"),

]
