from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    # Additional fields specific to departments

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    from teachers.models import Teacher   
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    No_of_students = models.IntegerField(default=0)
    # Additional fields related to grades

    def __str__(self):
        return self.name
    def grade_name(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Additional fields related to subjects

    def __str__(self):
        return self.name
