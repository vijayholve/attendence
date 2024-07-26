from django.contrib import admin
from .models import Student,Attendance ,CustomUser ,Teacher
# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Attendance) 


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from base.forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
