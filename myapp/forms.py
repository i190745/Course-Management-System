from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


DEPARTMENTS=(
            ("Computer Science","CS"),
            ("Artificial Intelligence","AI"),
            ("Cyber Security","CY"),
            ("Data Science","DS"),
            ("Software Engineering","SE"),
            ("Business Administration","BBA"),
            ("Accounting and Finance","AF"),
            ("Electrical Engineering","EE"),
            ("Robotics","RO")
)



class StudentForm(UserCreationForm):
    username=forms.CharField(label="Username",max_length=60,required=True)
    email=forms.EmailField(label="Email",max_length=60,required=True)
    name=forms.CharField(label="Full Name",max_length=100,required=True)
    batch=forms.IntegerField(label="Batch",min_value=16,max_value=21,required=True)
    roll_number=forms.IntegerField(label="Roll Number",min_value=1,required=True)
    department=forms.ChoiceField(choices=DEPARTMENTS,label="Department",required=True)

    
