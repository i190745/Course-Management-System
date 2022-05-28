
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def index(request):
    return render(request, "index.html")

def teacher_login(request):
    return render(request, "t_login.html")

def student_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['user'] = username
            return redirect('Student Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, "s_login.html")
    return render(request, "s_login.html")

def admin_login(request):
    return render(request, "adm_login.html")


def student_register(request):
    form=StudentForm()
    if request.method=='POST': 
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            email=request.POST['email']
            name=request.POST['name']
            batch=request.POST['batch']
            roll_number=request.POST['roll_number']
            department=request.POST['department']
            s=Student.objects.create(name=name,username=username,email=email,batch=batch,roll_number=roll_number,department=department)
            s.save()
            messages.success(request, 'Student has registered successfully ')
            return redirect('Student Login')
    
    return render(request, "s_register.html",{'form':form})

def teacher_register(request):
    return render(request, "t_register.html")


def student_dash(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    print(stu)
    return render(request, "s_dash.html",{'student':stu})
