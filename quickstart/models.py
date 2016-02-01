from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

class Group(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

# class Task(models.Model):
#     completed = models.BooleanField(default=False)
#     title = models.CharField(max_length=100)
