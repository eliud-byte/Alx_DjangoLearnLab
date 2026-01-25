from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from .models import Book, UserProfile

"""
Permissions and Group Configuration
Groups:
    - Viewers: Access to can_view. Can only see the book list.
    - Editors: Access to can_view, can_createm and can_edit. Can only
    add and modify entries but cannot remove them.
    - Admins: Full access including can_delete

Logic:> Permisssions are enforced at the view level using Django's
@permission_required decorator. If a user lacks the permission, a
'403 Forbidden' error is raised (raise_exception=True)
"""

@login_required
def edit_profile(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)

    # SECURITY CHECK: Ensure the logged-in user is the owner
    if request.user != profile.user:
        raise PermissionDenied # Sends a 403 Forbidden error
    
    if request.method == 'POST':
        # Logic to save changes would go here
        profile.bio = request.POST.get('bio')
        profile.save()
        return redirect('profile_detail', username=profile.user.username)
    
    return render(request, 'bookshelf/edit_profile.html', {'profile': profile})

# View for listing books (requested by can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View for creating a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # logic to create book
        pass
    return render(request, 'bookshelf/form_book.html')

# View for editing a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # logic to update book
        pass
    return render(request, 'bookshelf/form_book.html', {'book':book})

# View for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')