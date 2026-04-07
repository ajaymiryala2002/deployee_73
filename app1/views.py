from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# CREATE + READ
def student_list(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    context = {
        'students': students,
        'form': form
    }
    return render(request, 'list.html', context)


# UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'update.html', {'form': form})


# DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'delete.html', {'student': student})