from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200, default="Null")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

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
    

from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
