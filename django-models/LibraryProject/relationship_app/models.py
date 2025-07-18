from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200, default="Null")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=200, default="Null")
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=200, default="Null")
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name