
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Student,Teacher,Course,studentClasses, Admin
from .forms import StudentForm, TeacherForm,CourseForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    return render(request, "index.html")

def teacher_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            request.session['user']=username
            return redirect('Teacher Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 't_login.html')
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
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['user'] = username
            return redirect('Admin Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, "adm_login.html")
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
    form=TeacherForm()
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            email=request.POST['email']
            name=request.POST['name']
            department=request.POST['department']
            t=Teacher.objects.create(name=name,username=username,email=email,department=department)
            t.save()
            messages.success(request, 'Teacher has registered successfully ')
            return redirect('Teacher Login')
    return render(request, "t_register.html",{'form':form})

@login_required(login_url='Student Login')
def student_dash(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    return render(request, "s_dash.html",{'student':stu})

@login_required(login_url='Teacher Login')
def teacher_dash(request):
    user = request.session.get('user')
    t=Teacher.objects.get(username=user)
    return render(request, "t_dash.html",{'teacher':t})

@login_required(login_url='Admin Login')
def admin_dash(request):
    user = request.session.get('user')
    adm=admin.objects.get(username=user)
    return render(request, "adm_dash.html",{'admin':adm})

@login_required(login_url='Student Login')
def student_manage_acc(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    return render(request, "s_manage-acc.html",{'student':stu})

def student_logout(request):
    logout(request)
    return render(request, "s_logout.html")

@login_required(login_url='Student Login')
def student_delete_account(request):
    if request.method=='POST':
        user = request.session.get('user')
        u=User.objects.get(username=user)
        stu=Student.objects.get(username=user)
        u.delete()
        stu.delete()
        messages.success(request, "User Deleted Successfully")
        return redirect(request,'index1')
    
    return render(request, "s_delete_acc.html")

@login_required(login_url='Student Login')
def student_change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect('Student Dashboard')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, "s_change-password.html",{'form':form})

######### TEACHER
@login_required(login_url='Teacher Login')
def teacher_manage_acc(request):
    user = request.session.get('user')
    teach=Teacher.objects.get(username=user)
    return render(request, "t_manage-acc.html",{'teacher':teach})

def teacher_logout(request):
    logout(request)
    return render(request, "t_logout.html")

@login_required(login_url='Teacher Login')
def teacher_delete_account(request):
    if request.method=='POST':
        user = request.session.get('user')
        u=User.objects.get(username=user)
        t=Teacher.objects.get(username=user)
        u.delete()
        t.delete()
        messages.success(request, "User Deleted Successfully")
        return redirect(request,'index1')
    
    return render(request, "t_delete_acc.html")

@login_required(login_url='Teacher Login')
def teacher_change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect('Teacher Dashboard')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, "t_change-password.html",{'form':form})    


######### ADMIN
@login_required(login_url='Admin Login')
def admin_manage_acc(request):
    user = request.session.get('user')
    adm=Admin.objects.get(username=user)
    return render(request, "adm_manage-acc.html",{'admin':adm})

def admin_logout(request):
    logout(request)
    return render(request, "adm_logout.html")

@login_required(login_url='Admin Login')
def admin_delete_account(request):
    if request.method=='POST':
        user = request.session.get('user')
        u=User.objects.get(username=user)
        adm=Admin.objects.get(username=user)
        u.delete()
        adm.delete()
        messages.success(request, "User Deleted Successfully")
        return redirect(request,'index1')
    
    return render(request, "adm_delete_acc.html")

@login_required(login_url='Admin Login')
def admin_change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect('Admin Dashboard')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, "adm_change-password.html",{'form':form})    