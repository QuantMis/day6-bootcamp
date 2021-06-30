from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Courses, EnrolledCourses

@login_required(login_url="/login/")
def dashboard_courses_list(request):
    courses = Courses.objects.all()
    context = {
        "courses":courses
    }

    return render(request, "courses/courses_list.html", context)

@login_required(login_url="/login/")
def dashboard_enrolled_courses_list(request):
    enrolled_courses = EnrolledCourses.objects.all()
    context = {
        "enrolled_courses":enrolled_courses
    }

    return render(request, "courses/enrolled_courses.html", context)

@login_required(login_url="/login/")
def dashboard_performance(request):
    return render(request, "courses/performance.html")

@login_required(login_url="/login/")
def enroll_course(request, id):

    c = Courses.objects.get(id=id)

    create_new_enroll = EnrolledCourses.objects.create(course_name=c.course_name, course_category=c.course_category, course_diff=c.course_diff)

    courses = Courses.objects.all()
    context = {
        "courses":courses
    }

    return render(request, "courses/courses_list.html", context)

@login_required(login_url="/login/")
def unenroll_course(request, id):
    selected = EnrolledCourses.objects.get(id=id).delete()

    enrolled_courses = EnrolledCourses.objects.all()
    context = {
        "enrolled_courses":enrolled_courses
    }

    return render(request, "courses/enrolled_courses.html", context)


