from relationship_app.models import Author, Book

author = Author.objects.get(name="Chinua Achebe")
books = Book.objects.filter(author=author)

library = Library.objects.get(name="State Library")
books_in_library = library.books.all()

library = Library.objects.get(name="State Library")
librarian = library.librarian