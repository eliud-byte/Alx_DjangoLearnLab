from bookshelf.models import Book

# Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
print(book)

# Expected Output
1984 by George Orwell