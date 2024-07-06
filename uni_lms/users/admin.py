from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LmsUser


class CustomUserAdmin(UserAdmin):
    fields = list(UserAdmin.fieldsets)
    fields[1] = ('Personal info', {'fields': ('first_name', 'last_name', 'phone','email')})
    UserAdmin.fieldsets = tuple(fields)

admin.site.register(LmsUser, UserAdmin)









