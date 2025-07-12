from bookshelf.models import Book
retrieve_books = Book.objects.all()
print(retrieve_books)

success message:
<QuerySet [<Book: Book object (1)>]>
