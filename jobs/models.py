from django.db import models
from django.conf import settings
from django.db.models.enums import Choices

# Create your models here.

class Job(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=60)
    discription = models.TextField(max_length=155)
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    content = models.TextField()
    slug = models.SlugField(max_length=80)
    image = models.ImageField(upload_to="jobs/image/",)

    def __str__(self):
        return self.title
    
# class Applyform(models.Model):
#     id = models.AutoField
#     first_name = models.CharField(max_length=15)
#     last_name = models.CharField(max_length=15)
#     birth_date = models.CharField(max_length=10)
#     age = models.CharField(max_length=2)
#     education_completed = models.CharField(max_length=50)
#     pass_year = models.CharField(max_length=10)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField(max_length=254)
#     aadhar = models.IntegerField()
#     resume = models.FileField(upload_to="uploads/resumes/ %y / %m / % d",default="")
#     image = models.ImageField(upload_to="uploads/profiles/ %y / %m / % d",default="")
#     about = models.TextField(default="")
#     question = models.CharField(max_length=400,default="")

#     def __str__(self):
#         return self.first_name
    



    



