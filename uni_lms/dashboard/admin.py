from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import LmsUser
from .models import Student

class StudentAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('faculty', 'gpa', 'current_semester', 'subjects', 'gpa_history')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('first_name', 'last_name', 'email',
                       'phone', 'faculty', 'gpa', 'current_semester', 'subjects', 'gpa_history'),
        }),
    )
    
admin.site.register(Student, StudentAdmin)