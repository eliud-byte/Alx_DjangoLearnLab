from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, UserProfile

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for specific fields
    list_filter = ('author', 'publication_year')

    # Add search capability for title and author
    search_fields = ('title', 'author')

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
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
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')

    # Optional: Prevent admins from changing the 'user' field of an existing profile
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('user',)
        return ()
