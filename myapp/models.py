from django.db import models

# Create your models here.

#class CustomUser(AbstractUser):
#    user_type_data=((1,"Admin"),(2,"Teacher"),(3,"Staff"))
#    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


'''
class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    objects=models.Manager()

class Department(models.Model):
    dept_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    objects=models.Manager()

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    batch=models.IntegerField()
    roll_number=models.IntegerField()
    dept_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    objects=models.Manager()


class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    dept_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    objects=models.Manager()

class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    registration_limit=models.IntegerField()
    teacher_id=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    objects=models.Manager()

class prerequisite(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course")
    prerequisite_id=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="prerequisite")
    objects=models.Manager()

class CourseEnrollment(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    grade=models.FloatField()
    objects=models.Manager()

class CoursePassed(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    objects=models.Manager()
'''
