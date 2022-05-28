from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('s_login',views.student_login,name='Student Login'),
    path('t_login',views.teacher_login,name='Teacher Login'),
    path('adm_login',views.admin_login,name='Admin Login'),
    path('s_register',views.student_register,name='Student Register'),
    path('t_register',views.teacher_register,name='Teacher Register'),
    path('s_dash',views.student_dash,name='Student Dashboard')
]