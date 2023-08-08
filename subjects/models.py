from django.db import models
from departments.models import Department

class Subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept')
    # Additional fields specific to subjects

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Additional fields related to lessons

    def __str__(self):
        return self.title

class Resource(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resources/')
    # Additional fields related to resources

    def __str__(self):
        return self.title
