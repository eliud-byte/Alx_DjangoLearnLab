## Authentication System Overview:
1. **Registration:** Uses a `CustomUserCreationForm` inheriting from Django's `UserCreationForm` to capture usernames, email, and hashed passwords.
2. **Login/Logout:** Handled by Django's `auth_views`. Passwords are automatically checked against secure hashes in the database.
3. **Login/Logout:** A protected view using the @login_required decorator, ensuring only logged-in users can access `/profile`.
4. **Security:** All forms utilize {% csrf_token %} to prevent Cross-Site Request Forgery.

## How to Test:
1. Run `python manage.py runserver`.
2. Navigate to `/register` and create a user.
3. Login at `/login`. You should be redirected to `/profile`.
4. Try accessing `/profile` in an incognito window; it should force you back to the login page.