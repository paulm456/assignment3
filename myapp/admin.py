from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin




class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

# Register the CustomUser model in the admin interface
admin.site.register(CustomUser, CustomUserAdmin)



