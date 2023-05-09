from django.db import models

# Create your models here.


class University(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    city = models.CharField(blank=False, null=False, max_length=255)


class Lesson(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    time = models.TimeField()


class Group(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)


class Student(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255)
    second_name = models.CharField(blank=False, null=False, max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)


class Teacher(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255)
    second_name = models.CharField(blank=False, null=False, max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
