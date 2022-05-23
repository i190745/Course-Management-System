
from django.shortcuts import render
from django.http import HttpResponse
#from .models import Student
# Create your views here.

def index(request):
    return render(request, "index.html")

def teacher_login(request):
    return render(request, "t_login.html")

def student_login(request):
    return render(request, "s_login.html")

def admin_login(request):
    return render(request, "adm_login.html")

def student_register(request):
    return render(request, "s_register.html")

def teacher_register(request):
    return render(request, "t_register.html")

