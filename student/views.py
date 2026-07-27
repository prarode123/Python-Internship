from django.shortcuts import render, redirect
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


def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']

        Student.objects.create(
            name=name,
            course=course,
            email=email
        )

        return redirect('students')

    return render(request, 'student/add_student.html')


def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.course = request.POST['course']
        student.email = request.POST['email']

        student.save()

        return redirect('students')

    return render(request, 'student/edit_student.html', {
        'student': student
    })


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('students')