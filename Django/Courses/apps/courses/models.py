from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def valid(self, postData):
        errors = []
        if len(postData['name']) < 5:
            errors.append('Course name must be at least 5 characters')
        if len(postData['desc']) < 15:
            errors.append('Description must be at least 15 characters')
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()