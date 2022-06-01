from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from djangotoolbox.fields import ListField
# Create your models here.

#class CustomUser(AbstractUser):
#    user_type_data=((1,"Admin"),(2,"Teacher"),(3,"Staff"))
#    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class Student(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=100)
    email=models.EmailField(verbose_name="Email Address",max_length=60,unique=True,error_messages={'unique': ("Email Already Exists"),})
    batch=models.IntegerField(verbose_name="Batch")
    roll_number=models.IntegerField(verbose_name="")
    department=models.CharField(verbose_name="Department",max_length=60)
    

class Teacher(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=100)
    email=models.EmailField(verbose_name="Email Address",max_length=60,unique=True,error_messages={'unique': ("Email Already Exists"),})
    department=models.CharField(verbose_name="Department",max_length=60)

class Admin(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=100)
    email=models.EmailField(verbose_name="Email Address",max_length=60,unique=True,error_messages={'unique': ("Email Already Exists"),})

class Course(models.Model):
    course_id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=255)
    prerequisite=models.CharField(max_length=10)
    teacher=models.CharField(max_length=20)
    registration_limit=models.IntegerField()
    department=models.CharField(verbose_name="Department",max_length=60)
    #students=ListField()

class studentClasses(models.Model):
    course_id=models.CharField(max_length=10)
    student=models.CharField(max_length=20)

class teacherClass(models.Model):
    course_id=models.CharField(max_length=10)
    teacher=models.CharField(max_length=20)

