from bookshelf.models import Book

# Retrieve the book
t = Book.objects.get(title="1984")

# Verify
print(t.title, t.author, t.publication_year)

# Expected Output
1984 George Orwell 1949
