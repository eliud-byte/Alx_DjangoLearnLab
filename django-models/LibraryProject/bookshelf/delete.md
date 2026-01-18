from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
all_books = Book.objects.all()
print(all_books)

# Expected Output
<QuerySet []>