from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class ModelAdmin(UserAdmin):
    model = CustomUser
    
    # list_display: Fields shown in the user list table
    list_display = ['email', 'username', 'date_of_birth', 'is_staff']

    # fieldsets controls the "Change User" page
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Extra Profile Info', {'fields': ('date_of_birth', 'profile_photo')}),
    ]

    # add_fieldsets controls the "Add User" page
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ('Extra Profile Info', {'fields': ('date_of_birth', 'profile_photo')}),
    ]

# Register the model using the custom Admin class
admin.site.register(CustomUser, ModelAdmin)