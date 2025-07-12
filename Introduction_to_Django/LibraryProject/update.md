from bookshelf.models import Book
update_book = Book.objects.get(id=1)
update_book.title = 'Nineteen Eighty-Four'
update_book.save()
print(update_book.title)

Output:
Nineteen Eighty-Four