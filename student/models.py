from django.db import models
from school.models import Data
import datetime
import random
# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    reg_number = models.CharField(max_length=5)
    dob = models.CharField(max_length=30,verbose_name='date of birth')
    data = models.ForeignKey(Data,on_delete=models.CASCADE,null=True,blank=True)
    from departments.models import Grade
    std_class =  models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True,blank=True)
    from teachers.models import Teacher   
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    state_of_origin = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    
    
    
    # guardians = models.ForeignKey()
    # medicalInfo=models.JSONField()
    def __str__(self):
        name = f'{self.firstname} {self.lastname} {self.id}'
        return name
    def full_name(self):
        name = f'{self.firstname} {self.lastname}'
        return name
    def save(self,*args,**kwargs):
        date=datetime.datetime.now()
        reg = int(date.year)+int(random.randrange(100,999))+int(self.std_class.id)
        reg = str(reg)
        same_reg = Student.objects.filter(reg_number=reg)
        if not same_reg:
            self.reg_number=reg
        super().save(*args,**kwargs)
    def get_image(self):
        return self.data.photo.url
    def get_teacher(self):
        if self.teacher is None:
            return ""
        return self.teacher.get_teachers_name()


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()
    
    def __str__(self):
        return f"{self.student} - {self.date}"
class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    # Additional fields related to academic records

    def __str__(self):
        return f"{self.student} - {self.subject}"
    
class Guardian(models.Model):
    name = models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    data = models.ForeignKey(Data,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    
  
    

    