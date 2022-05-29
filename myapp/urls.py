from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index1'),
    path('s_login',views.student_login,name='Student Login'),
    path('t_login',views.teacher_login,name='Teacher Login'),
    path('adm_login',views.admin_login,name='Admin Login'),
    path('s_register',views.student_register,name='Student Register'),
    path('t_register',views.teacher_register,name='Teacher Register'),
    path('s_dash',views.student_dash,name='Student Dashboard'),
    path('t_dash',views.teacher_dash,name='Teacher Dashboard'),
    path('adm_dash',views.admin_dash,name='Admin Dashboard'),
    path('s_manage_acc',views.student_manage_acc,name='Student Manage Account'),
    path('t_manage_acc',views.teacher_manage_acc,name='Teacher Manage Account'),
    path('adm_manage_acc',views.admin_manage_acc,name='Admin Manage Account'),
    path('s_logout',views.student_logout,name='Student Logout'),
    path('t_logout',views.teacher_logout,name='Teacher Logout'),
    path('adm_logout',views.admin_logout,name='Admin Logout'),
    path('s_change_password',views.student_change_password,name='Student Change Password'),
    path('t_change_password',views.teacher_change_password,name='Teacher Change Password'),
    path('adm_change_password',views.admin_change_password,name='Admin Change Password'),
    path('s_delete_account',views.student_delete_account,name='Student Delete Account'),
    path('t_delete_account',views.teacher_delete_account,name='Teacher Delete Account'),
    path('adm_delete_account',views.admin_delete_account,name='Admin Delete Account')
]