from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based View for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            return redirect('list_books') # Redirect to main page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions for role checking
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'relationship_profile') and user.relationship_profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'relationship_profile') and user.relationship_profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'relationship_profile') and user.relationship_profile.role == 'Member'

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librrian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# View to add a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for adding a book
    return render(request, 'relationship_app/add_book.html')

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for editing the book 
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for deleting the book
    return render(request, 'relationship_app/delete_book.html', {'book': book})
