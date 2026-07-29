from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Student
from .forms import StudentForm


# def home(request):
#     return render(request, 'student/home.html')

def home(request):

    total_students = Student.objects.count()

    total_courses = Student.objects.values(
        'course'
    ).distinct().count()

    recent_students = Student.objects.order_by(
        '-id'
    )[:5]

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'recent_students': recent_students,
    }

    return render(request, 'student/home.html', context)


def about(request):
    return render(request, 'student/about.html')


def contact(request):
    return render(request, 'student/contact.html')


@login_required
def students(request):

    search = request.GET.get('search', '')

    student_list = Student.objects.all()

    if search:
        student_list = student_list.filter(name__icontains=search)

    student_list = student_list.order_by('name')

    paginator = Paginator(student_list, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

    return render(request, 'student/students.html', {
        'students': students,
        'search': search
    })


@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('students')

    else:
        form = StudentForm()

    return render(request, 'student/add_student.html', {
        'form': form
    })


@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('students')

    else:
        form = StudentForm(instance=student)

    return render(request, 'student/edit_student.html', {
        'form': form
    })


@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    messages.success(request, "Student deleted successfully!")

    return redirect('students')