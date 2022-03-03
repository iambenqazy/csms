from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentDetail
from .forms import StudentDetailForm


# Create your views here.

def students_list(request):
    students = StudentDetail.objects.all()
    context = {'students': students}
    return render(request, 'transcripts/students-list.html', context)


def student(request, pk):
    student_obj = StudentDetail.objects.get(id=pk)
    return render(request, 'transcripts/single-student.html', {'student': student_obj})


def create_student(request):
    form = StudentDetailForm()

    if request.method == 'POST':
        form = StudentDetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students-list')
    context = {'create_form': form}
    return render(request, 'transcripts/forms.html', context)


def update_student_detail(request, pk):
    single_student = StudentDetail.objects.get(id=pk)
    form = StudentDetailForm(instance=single_student)

    if request.method == 'POST':
        form = StudentDetailForm(request.POST, request.FILES, instance=single_student)
        if form.is_valid():
            form.save()
            return redirect('students-list')

    context = {'create_form': form}
    return render(request, 'transcripts/forms.html', context)


def delete_student(request, pk):
    single_student = StudentDetail.objects.get(id=pk)
    if request.method == 'POST':
        single_student.delete()
        return redirect('students-list')
    context = {'delete_student': single_student}
    return render(request, 'transcripts/delete-form.html', context)
