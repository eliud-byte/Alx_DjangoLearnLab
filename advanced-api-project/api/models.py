from django.db import models

class Author(models.Model):
    """
    Represents a book author.
    Has a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an Author.
    The foreign key links each book to a single author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # related_name='books' allows us to access books from an author instance (author.books.all())
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title