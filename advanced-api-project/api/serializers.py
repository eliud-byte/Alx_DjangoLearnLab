from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model.
    Includes custom validation for the publication year.
    """
    class Meta:
        model = Book 
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Checks that the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.
    Includes a nested BookSerializer to show all books related to the author.
    """
    # The field name 'books' matches the related_name in the Book model
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']