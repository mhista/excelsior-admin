from django.db import models
from school.file_upload import item_uploads
# Create your models here.

class Data(models.Model):
    gender = models.CharField(max_length=1,null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    photo = models.ImageField(upload_to=item_uploads,null=True)
    age = models.CharField(max_length=2,null=True)
    unique_ref = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.id)