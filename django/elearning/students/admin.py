from django.contrib import admin
from students.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    pass

admin.site.register(User, UserAdmin)