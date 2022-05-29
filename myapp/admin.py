from django.contrib import admin
from myapp.models import Student,Teacher,Admin,studentClasses,Course
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(studentClasses)
admin.site.register(Course)
