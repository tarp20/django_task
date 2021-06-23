from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=249)


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        ''' makes unable to edit '''

        if self.pk is None:
            super(Student, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('index')


class Course(models.Model):
    name = models.CharField(max_length=249)
    students = models.ManyToManyField(Student, through='Connect')

    def __str__(self):
        return f'{self.name}'


class Connect(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
