from bookshelf.models import Book
delete_book = Book.objects.get(id=1)
delete_book.delete()
output:
(1, {'bookshelf.Book': 1})


print(retrieve_books)
output:
<QuerySet []>
