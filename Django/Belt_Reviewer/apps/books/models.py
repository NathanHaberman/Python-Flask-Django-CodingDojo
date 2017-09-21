from __future__ import unicode_literals
from ..login_and_registration.models import User
from django.db import models

# Create your models here.
class AuthorManager(models.Manager):
    def valid(self, postData):
        errors = []
        if len(postData['new_author']) < 1 and postData['author'] == '':
            errors.append("Please select or enter an author")
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255)

    objects = AuthorManager()



class BookManager(models.Manager):
    def valid(self, postData):
        errors =[]
        if len(postData['title']) < 1:
            errors.append('Please enter a title')
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=None, related_name='written_book')

    objects = BookManager()



class ReviewManager(models.Manager):
    def valid(self, postData):
        errors = []
        if len(postData['content']) < 15:
            errors.append('Review must be at least 15 characters')
        return errors

class Review(models.Model):
    content = models.TextField()
    stars = models.IntegerField()
    reviewed_book = models.ForeignKey(Book, on_delete=None, related_name='review')
    reviewer = models.ForeignKey(User, on_delete=None, related_name='review')
    created_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()