# Django Blog Project

A comprehensive blogging platform built with Django, featuring user authentication, post management (CRUD), and an interactive comment system.

## Features

### 1. User Authentication:
- **Registration & Login:** Users can create accounts and log in to access their personalized features
- **Profile Management:** Authenticated users can view and update their profile details.

### 2. Post Mnagement (CRUD)
- **Create:** Authenticated users can create new blog posts via `PostCreateView`.
- **Read:** All visitors can view a list of posts (`PostListView`) or individual post details (`PostDetailView`)
- **Update/Delete:** Only the original author of a post has permission to edit or remove it, enforced by Django's `UserPassesTestMixin`.

### 3. Comment System
- Users can engage with posts by leaving comments.
- **Permissions:** Any authenticated user can comment, but only the comment author can edit or delete their own feedback.
- **Relationship:** The `Comment` model uses a ForeignKey to link specific `Post` instances and `User` accounts.

## Installaion & Setup
1. Clone the repository: `git clone http://github.com/Alx_DjangoLearnLab/django_blog`
2. Install dependencies: `pip install django`
3. Apply migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## Testing the features
- **Posts:** Navigate to `/post/new/` while logged in to create a post. Try to edit a post created by another user to verify permission restrictions.
- **Comments:** Open a post's detail page and use the "Add a Comment" link. Verify that the "Edit" and "Delete" buttons only appear for your own comments.

## Tagginh & Search Features:
- **Tagging:** Implemented a custom `Tag` model. The `PostForm` was overridden to accept a comma-seperated string of tags. The `save()` method processes this string, creating new `tag` objects on the fly if they don't exist and associating them with the post.
- **Search:** The search view uses `django.db.models.Q` to perform complex lookups. A single query checks if the search term exists in the post Title OR Content Tags.
- **Usage:**
    - **Add Tags:** When creating/editing a post, type tags into the "Tags" field seperated by commas (e.g., "News, Updates, Python").
    - **Search:** Use the search bar in the navigation menu.