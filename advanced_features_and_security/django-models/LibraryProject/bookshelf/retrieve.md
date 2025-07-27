from bookshelf.models import Book

retrieve_books = Book.objects.get(title = "1984")
print(retrieve_books)

success message:
<QuerySet [<Book: Book object (1)>]>
