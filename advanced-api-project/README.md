# Advanced API Project - Book Management System

This project is a Django REST Framework API for managing Authors and their Books. It demonstrates advanced serialization techniques and generic views.

## Features
- **Author & Book Models:** One-to-many relationship (Author has many books).
- **Nested Serializers:** The Author API response includes a full list of books written by that author.
- **Data Validation:** Custom validation ensures books cannot have a publication year in the future.
- **Permission-Based Access:** 
    * **Public:** Viewing the list of books or spicific book details.
    * **Restricted:** Creating, updating, or deleting books requires user authentication.

## API Endpoints

### Books
| Endpoint | Method | Description | Permission |
| :--- | :--- | :--- | :--- |
| `/api/books/` | GET | List all books | Public |
| `/api/books/<id>/` | GET | Get book details | Public |
| `/api/books/create/` | POST | Add a new book | Authenticated |
| `/api/books/update/<id>/` | PUT/PATCH | Update a book | Authenticated |
| `/api/books/delete/<id>/` | DELETE | Delete a book | Authenticated |

## Setup Instructions
1. Install requirements: `pip install django djangorestframework`
2. Run migrations: `python manage.py migrate`
3. Create an admin: `python manage.py createsuperuser`
4. Start server: `python manage.py runserver`

## Advanced Quering
The `/api/books/` endpoint supports the following features:

- **Filtering:** Use `?title=`, `?author=`, or `?publication_year=` to filter results.
- **Searching:** Use `?search=` to perform  text search across titles and author names.
- **Ordering:** Use `?ordering=` to sort results by `title` or `publication_year`. Prefix with `-` for descending order (e.g., `?ordering=-title`).

## Testing
This project uses Django's built-in test runner to verify API finctionality.

To run the tests:
`python manage.py test api`

**What is tested:**
- **CRUD Operations:** Verifies that books can be created, read, updated, and deleted.
- **Permissions:** Ensures only authenticated users can modify data.
- **Search/Filter/Order:** Verifies that query parameters filter the results correctly.