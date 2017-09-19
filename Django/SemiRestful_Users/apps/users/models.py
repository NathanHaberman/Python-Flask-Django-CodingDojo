from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def valid(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append('First name must be longer than 2 characters')
        if len(postData['last_name']) < 2:
            errors.append('Last name must be longer than 2 characters')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()