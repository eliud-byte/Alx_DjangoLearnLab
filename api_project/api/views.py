from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """
    If one used 'IsAuthenticatedOrReadOnly', strangers could read
    the books but only logged-in users could edit them. 
    'IsAuthenticated' blocks strangers completely.
    """
    # This line locks the view. Only users with a token (or login) can access it.
    permission_classes = [IsAuthenticated]
