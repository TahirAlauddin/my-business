from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdminConfig(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ['-start_date']
    list_display = ['email','username', 'contact', 'is_staff', 'is_active']
    
    fieldsets = (
        (None, {'fields':('email', 'username')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
        ('Personal', {'fields':('about', 'contact', 'address')})
    )

    add_fieldsets = (
                (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'contact',
            'address', 'password1', 'password2',
            'is_active', 'is_staff')}
        ),
    )

        
        
admin.site.register(CustomUser, CustomUserAdminConfig)