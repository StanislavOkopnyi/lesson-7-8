from django.contrib import admin
from .models import University, Lesson, Group, Student, Teacher

# Register your models here.
admin.site.register(University)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
