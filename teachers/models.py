from django.db import models
from departments.models import Department
from school.models import Data

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=10,null=True)
    data = models.ForeignKey(Data(),on_delete=models.CASCADE,null=True,blank=True)
    # Additional fields specific to teachers

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_teachers_name(self):
        return f"{self.first_name} {self.last_name}"

class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    # Additional fields related to assignments

    def __str__(self):
        return self.title

class Grading(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    # Additional fields related to grading

    def __str__(self):
        return f"{self.assignment} - {self.student}"

