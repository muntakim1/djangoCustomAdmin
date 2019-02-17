from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    filter_list=('student_id','name')

admin.site.register(Student,StudentAdmin)