from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
			errors['first_name'] = "First name must be at least 2 characters long"
        if len(post_data['last_name']) < 2:
			errors['last_name'] = "Last name must be at least 2 characters long"
        if not re.match(EMAIL_REGEX, post_data['email']):
			errors['email'] = "Email must be of correct format."
        if len(post_data['password']) < 8:
			errors['password'] = "Password must be at least 8 characters long"
        if post_data['password'] != post_data['confirm']:
			errors['password'] = "Password must match password confirmation field"
        print errors
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
