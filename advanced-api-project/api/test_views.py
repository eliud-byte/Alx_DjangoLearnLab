# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    
    def setUp(self):
        """
        Set up the test environment before each test method runs.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create a test author
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        
        # Create a test book
        self.book = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author
        )
        
        # URLs for list and detail views
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book_authenticated(self):
        """
        Ensure an authenticated user can create a book.
        """
        self.client.login(username='testuser', password='password')
        data = {
            "title": "The Fellowship of the Ring",
            "publication_year": 1954,
            "author": self.author.pk
        }
        response = self.client.post(self.list_url + "create/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], "The Fellowship of the Ring")  # type: ignore

    def test_create_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a book.
        """
        data = {
            "title": "The Two Towers",
            "publication_year": 1954,
            "author": self.author.pk
        }
        response = self.client.post(self.list_url + "create/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """
        Ensure an authenticated user can update a book.
        """
        self.client.login(username='testuser', password='password')
        data = {
            "title": "The Hobbit (Updated)",
            "publication_year": 1937,
            "author": self.author.pk
        }
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db() # Reload data from DB
        self.assertEqual(self.book.title, "The Hobbit (Updated)")

    def test_delete_book_authenticated(self):
        """
        Ensure an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='password')
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_year(self):
        """
        Test filtering books by publication year.
        """
        # Create another book with a different year
        Book.objects.create(title="Recent Book", publication_year=2023, author=self.author)
        
        # Filter for 1937
        response = self.client.get(self.list_url, {'publication_year': 1937})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should only find the one book from setUp
        self.assertEqual(len(response.data), 1)  # type: ignore
        self.assertEqual(response.data[0]['title'], "The Hobbit")  # type: ignore

    def test_search_books(self):
        """
        Test searching books by title.
        """
        Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        
        response = self.client.get(self.list_url, {'search': 'Hobbit'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # type: ignore
        self.assertEqual(response.data[0]['title'], "The Hobbit")  # type: ignore

    def test_ordering_books(self):
        """
        Test ordering books by publication year.
        """
        book2 = Book.objects.create(title="Silmarillion", publication_year=1977, author=self.author)
        
        # Order by year ascending
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "The Hobbit")  # type: ignore  # 1937
        self.assertEqual(response.data[1]['title'], "Silmarillion")  # type: ignore  # 1977