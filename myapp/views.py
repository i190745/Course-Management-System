
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Student,Teacher,Course,studentClasses, Admin, teacherClass
from .forms import StudentForm, TeacherForm,CourseForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html")

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



@login_required(login_url='Student Login')
def student_dash(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    return render(request, "s_dash.html",{'student':stu})



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

@login_required(login_url='Student Login')
def student_enroll_course(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    courses=Course.objects.filter(department=stu.department)
    if request.method=='POST':
        cid=request.POST['courseid']
        if Course.objects.filter(course_id=cid).exists():
            if studentClasses.objects.filter(course_id=cid,student=stu.username).exists():
                messages.info(request, "Student Already Registered In Course") 
            else:
                c_s=studentClasses.objects.create(course_id=cid,student=stu.username)
                c_s.save()
                messages.success(request, stu.name + "Successfully Enrolled to "+cid)
        else:
            messages.info(request, "Course Does Not Exist") 
    return render(request, "s_enroll.html",{'courses':courses})

@login_required(login_url='Student Login')
def student_drop_course(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    c_s=studentClasses.objects.filter(student=stu.username)
    c_list=Course.objects.all()
    if request.method=='POST':
        cid=request.POST['courseid']
        if not studentClasses.objects.filter(student=stu.username).exists() and Course.objects.filter(course_id=cid).exists():
            messages.info(request, "Not Enrolled In This Course")
        elif not studentClasses.objects.filter(course_id=cid).exists():
            messages.info(request, "Course Does Not Exist")
        else:
            row=studentClasses.objects.filter(course_id=cid,student=stu.username)
            row.delete()
            messages.info(request, stu.name + "Successfully Dropped "+cid) 
    return render(request, "s_drop.html",{'courses':c_list,'c_s':c_s,'student':stu})

@login_required(login_url='Student Login')
def student_view_courses(request):
    user = request.session.get('user')
    stu=Student.objects.get(username=user)
    c_s=studentClasses.objects.filter(student=stu.username)
    c_list=Course.objects.all()
    return render(request, "s_view_courses.html",{'courses':c_list,'c_s':c_s,'student':stu})

######### TEACHER
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

@login_required(login_url='Teacher Login')
def teacher_manage_acc(request):
    user = request.session.get('user')
    teach=Teacher.objects.get(username=user)
    return render(request, "t_manage-acc.html",{'teacher':teach})

def teacher_logout(request):
    logout(request)
    return render(request, "t_logout.html")

@login_required(login_url='Teacher Login')
def teacher_dash(request):
    user = request.session.get('user')
    t=Teacher.objects.get(username=user)
    return render(request, "t_dash.html",{'teacher':t})

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

######## 
@login_required(login_url='Teacher Login')
def teacher_view_courses(request):
    user = request.session.get('user')
    teacher=Teacher.objects.get(username=user)
    c_list=teacherClass.objects.all()
    if request.method=='POST':
        cid=request.POST['cid']
        c_s=studentClasses.objects.filter(course_id=cid)
        students=Student.objects.all()
        return render(request,'t_view-courses.html',{'cid':cid,'courses':c_s,'students':students})

    return render(request, "t_select-course.html",{'courses':c_list})

@login_required(login_url='Teacher Login')
def teacher_upload_lectures(request):
    user = request.session.get('user')
    teacher=Teacher.objects.get(username=user)
    c_list=teacherClass.objects.all()
    if request.method=='POST':
        cid=request.POST['cid']
        messages.success(request, "Lecture Has Been Uploaded")
        return render(request, "t_upload-lectures.html",{'cid':cid})
    return render(request, "t_select-course.html",{'courses':c_list})

######### ADMIN

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


@login_required(login_url='Admin Login')
def admin_manage_acc(request):
    user = request.session.get('user')
    adm=Admin.objects.get(username=user)
    return render(request, "adm_manage-acc.html",{'admin':adm})

def admin_logout(request):
    logout(request)
    return render(request, "adm_logout.html")


@login_required(login_url='Admin Login')
def admin_dash(request):
    user = request.session.get('user')
    adm=Admin.objects.get(username=user)
    return render(request, "adm_dash.html",{'admin':adm})

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
    
    return render(request, "adm_delete-acc.html")

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
    return render(request, "adm_change_password.html",{'form':form})    

@login_required(login_url='Admin Login')
def admin_manage_courses(request):
    return render(request, "adm_manage_courses.html")    


@login_required(login_url='Admin Login')
def admin_add_course(request):
    form=CourseForm()
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            cid=request.POST['course_id']
            cname=request.POST['name']
            dept=request.POST['department']
            course=Course.objects.create(course_id=cid,name=cname,department=dept)
            course.save()
            messages.success(request, 'Course added successfully ')  
            return redirect('Admin Manage Courses')

    return render(request, "adm_add_course.html",{'form':form})    

@login_required(login_url='Admin Login')
def admin_remove_course(request):
    courses=Course.objects.all()
    if request.method=='POST':
        cid=request.POST['courseid']
        if Course.objects.filter(course_id=cid).exists():
            c=Course.objects.filter(course_id=cid)
            c.delete()
            messages.success(request, 'Course Removed Successfully')
        else:     
            messages.info(request, "Course ID does not Exist") 
    return render(request, "adm_remove-course.html",{'courses':courses})

@login_required(login_url='Admin Login')
def admin_specify_prerequisite(request):
    courses=Course.objects.all()
    if request.method=='POST':
        cid=request.POST['courseid']
        pid=request.POST['prereq']
        if Course.objects.filter(course_id=cid).exists() and Course.objects.filter(course_id=pid).exists():
            c=Course.objects.filter(course_id=cid)
            c.update(prerequisite=pid)
            messages.success(request, 'Prerequisite Added Successfully')
        else:
            messages.info(request, "Course or PreRequisite does not Exist") 

    return render(request, "adm_specify-prerequisite.html",{'courses':courses})

@login_required(login_url='Admin Login')
def admin_select_course(request):
    c_list=Course.objects.all()    
    if request.method=='POST':
        cid=request.POST['cid']
        c_s=studentClasses.objects.filter(course_id=cid)
        students=Student.objects.all()
        if teacherClass.objects.filter(course_id=cid).exists():
            teacher=teacherClass.objects.filter(course_id=cid)
        else:
            teacher="Not Assigned"
        return render(request,'adm_view-course.html',{'courses':c_s,'students':students,'t':teacher})
    return render(request, "adm_select-course.html",{'courses':c_list})


@login_required(login_url='Admin Login')
def admin_add_student_course(request):
    if request.method=='POST':
        cid=request.POST['courseid']
        stu=request.POST['student']
        if not Student.objects.filter(username=stu).exists():
            messages.info(request, "Student Does Not Exist")
        elif not Course.objects.filter(course_id=cid).exists():
            messages.info(request, "Course Does Not Exist")
        elif studentClasses.objects.filter(course_id=cid,student=stu).exists():
            messages.info(request, stu+" already enrolled in "+cid )
        else:
            s_c=studentClasses.objects.create(student=stu,course_id=cid)
            s_c.save()
            messages.success(request, stu+" added to "+cid)
            return redirect("Admin Select Course")
    return render(request, "adm_add-student-course.html")

@login_required(login_url='Admin Login')
def admin_remove_student_course(request):

    if request.method=='POST':
        cid=request.POST['courseid']
        stu=request.POST['student']
        if not Student.objects.filter(username=stu).exists():
            messages.info(request, "Student Does Not Exist")
        elif not Course.objects.filter(course_id=cid).exists():
            messages.info(request, "Course Does Not Exist")
        elif not studentClasses.objects.filter(course_id=cid,student=stu).exists():
            messages.info(request, stu+" not enrolled in "+cid )
        else:
            s_c=studentClasses.objects.filter(course_id=cid,student=stu)
            s_c.delete()
            messages.success(request, stu+" removed from "+cid)
            return redirect("Admin Select Course")

    return render(request, "adm_remove-student-course.html")

@login_required(login_url='Admin Login')
def admin_add_teacher_course(request):
    if request.method=='POST':
        cid=request.POST['courseid']
        stu=request.POST['teacher']
        if not Teacher.objects.filter(username=stu).exists():
            messages.info(request, "Teacher Does Not Exist")
        elif not Course.objects.filter(course_id=cid).exists():
            messages.info(request, "Course Does Not Exist")
        elif teacherClass.objects.filter(course_id=cid,teacher=stu).exists():
            messages.info(request, stu+" Already Teaches "+cid )
        else:
            s_c=teacherClass.objects.create(course_id=cid,teacher=stu)
            s_c.save()
            messages.success(request, stu+" Teaches "+cid)
            return redirect("Admin Select Course")
    return render(request, "adm_add-teacher-course.html")

@login_required(login_url='Admin Login')
def admin_remove_teacher_course(request):
    if request.method=='POST':
        cid=request.POST['courseid']
        stu=request.POST['teacher']
        if not Teacher.objects.filter(username=stu).exists():
            messages.info(request, "Teacher Does Not Exist")
        elif not Course.objects.filter(course_id=cid).exists():
            messages.info(request, "Course Does Not Exist")
        elif not teacherClass.objects.filter(course_id=cid,teacher=stu).exists():
            messages.info(request, stu+" Does Not Teach "+cid )
        else:
            s_c=teacherClass.objects.filter()(course_id=cid,teacher=stu)
            s_c.delete()
            messages.success(request, stu+" Removed As Teacher "+cid)
            return redirect("Admin Select Course")
    return render(request, "adm_remove-teacher-course.html")