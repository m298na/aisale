from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Deal, Task, Call, Message, Employee


class EmployeeAdmin(UserAdmin):
    model = Employee
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'position', 'phone', 'hire_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'position', 'phone', 'hire_date', 'is_active', 'is_staff')}
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


admin.site.register(Client)
admin.site.register(Deal)
admin.site.register(Task)
admin.site.register(Call)
admin.site.register(Message)
admin.site.register(Employee, EmployeeAdmin)
