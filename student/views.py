from django.shortcuts import render
from .models import Student


def home(request):
    return render(request, 'student/home.html')


def about(request):
    return render(request, 'student/about.html')


def contact(request):
    return render(request, 'student/contact.html')


def students(request):
    student_list = Student.objects.all()

    return render(request, 'student/students.html', {
        "students": student_list
    })