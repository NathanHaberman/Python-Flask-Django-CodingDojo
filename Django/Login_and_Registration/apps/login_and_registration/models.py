from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append('First name has to be at least 2 characters')
        elif len(postData['first_name']) > 255:
            errors.append('First name is too long')
        if len(postData['last_name']) < 2:
            errors.append('Last name has to be at least 2 characters')
        elif len(postData['last_name']) > 255:
            errors.append('Last name is too long')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Not a vaild email')
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords do not match')
        elif len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters')
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    objects = UserManager()