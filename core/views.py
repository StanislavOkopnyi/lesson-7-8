from django.shortcuts import render
from .models import Student, Teacher
from django.views import View
# Create your views here.


def all_students(request):
    students = [i for i in Student.objects.all()]
    return render(
        request,
        "students.html",
        context={"students": students},
    )


class TeachersView(View):

    def get(self, request):
        teachers = [i for i in Teacher.objects.all()]
        return render(
            request,
            "teachers.html",
            context={"teachers": teachers}
        )
