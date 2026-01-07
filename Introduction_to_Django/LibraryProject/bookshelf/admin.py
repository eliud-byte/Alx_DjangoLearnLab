from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for specific fields
    list_filter = ('author', 'publication_year')

    # Add search capability for title and author
    search_fields = ('title', 'author')

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)