from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index1'),
    path('s_register',views.student_register,name='Student Register'),
    path('s_login',views.student_login,name='Student Login'),
    path('s_logout',views.student_logout,name='Student Logout'),
    path('s_dash',views.student_dash,name='Student Dashboard'),
    path('s_manage_acc',views.student_manage_acc,name='Student Manage Account'),
    path('s_change_password',views.student_change_password,name='Student Change Password'),
    path('s_delete_account',views.student_delete_account,name='Student Delete Account'),
    path('s_view_courses',views.student_view_courses,name='Student View Courses'),
    path('s_enroll',views.student_enroll_course,name='Student Enroll Course'),
    path('s_drop',views.student_drop_course,name='Student Drop Course'),
    
    path('t_register',views.teacher_register,name='Teacher Register'),
    path('t_login',views.teacher_login,name='Teacher Login'),
    path('t_logout',views.teacher_logout,name='Teacher Logout'),
    path('t_dash',views.teacher_dash,name='Teacher Dashboard'),
    path('t_manage_acc',views.teacher_manage_acc,name='Teacher Manage Account'),
    path('t_change_password',views.teacher_change_password,name='Teacher Change Password'),
    path('t_delete_account',views.teacher_delete_account,name='Teacher Delete Account'),
    path('t_view-courses',views.teacher_view_courses,name='Teacher View Courses'),


    path('adm_login',views.admin_login,name='Admin Login'),
    path('adm_logout',views.admin_logout,name='Admin Logout'),
    path('adm_dash',views.admin_dash,name='Admin Dashboard'),
    path('adm_manage_acc',views.admin_manage_acc,name='Admin Manage Account'),
    path('adm_change_password',views.admin_change_password,name='Admin Change Password'),
    path('adm_delete_account',views.admin_delete_account,name='Admin Delete Account'),
    path('adm_manage_courses',views.admin_manage_courses,name='Admin Manage Courses'),
    path('adm_add_course',views.admin_add_course,name='Admin Add Course'),
    path('adm_remove_course',views.admin_remove_course,name='Admin Remove Course'),
    path('adm_specify_prerequisite',views.admin_specify_prerequisite,name='Admin Specify Prerequisite'),
    path('adm_select_course',views.admin_select_course,name='Admin Select Course'),
    path('adm_add_student_course',views.admin_add_student_course,name='Admin Add Student Course'),
    path('adm_remove_student_course',views.admin_remove_student_course,name='Admin Remove Student Course'),
    path('adm_add_teacher_course',views.admin_add_teacher_course,name='Admin Add Teacher Course'),
    path('adm_remove_teacher_course',views.admin_remove_teacher_course,name='Admin Remove Teacher Course')


]