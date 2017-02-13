from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Lecture(models.Model):
    name = models.CharField(max_length=40)
    week = models.IntegerField()
    course = models.ForeignKey(Course)
    url = models.TextField()
