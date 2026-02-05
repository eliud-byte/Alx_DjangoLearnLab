from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List view for Books with advanced query capabilities.
    Allows:
    - Filtering by title, author name, and publication_year
    - Searching by title and author's name.
    - Ordering by title and publication_year.
    Permissions: Allow any user (Read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Define the backends for filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    #Filtering: Exact matches or specified fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching: Text-based search across specific fields
    # Use 'author__name' to search through the related Author model
    search_fields = ['title', 'author__name']

    # Ordering: Allow users to sort by these fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Permissions: Allow any user (Read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Permissions: IsAuthenticated (Only logged-in users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # You can add custom ligic here, like setting the user
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Modify an existing book.
    Permissions: IsAuthenticated.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Remove a book from the database.
    Permissions: IsAuthenticated.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]