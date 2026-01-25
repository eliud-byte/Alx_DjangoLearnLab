from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import UserProfile

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
