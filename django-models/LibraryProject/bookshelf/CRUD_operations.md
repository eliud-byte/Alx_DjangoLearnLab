# CRUD  Operations for Book Model

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984 by George Orwell

t = Book.objects.get(title="1984")
print(t.title, t.author, t.publication_year)
# Output: 1984 George Orwell 1949

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
all_books = Book.objects.all()
print(all_books)
# Output: <QuerySet []>

