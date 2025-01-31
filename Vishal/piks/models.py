from django.db import models

# Create your models here.

class User(models.Model):
   usr_heading = models.CharField(max_length=100)
   usr_description = models.CharField(max_length=100)
   usr_code_box = models.CharField(max_length=100)
   usr_image = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.usr_heading