# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

# NAME_REGEX = re.compile(r'^{1,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PHONE_REGEX = re.compile(r'^[(]+\d{3}[)]+\d{3}[-]+\d{4}$')

class ClientManager(models.Manager):
    def client_valid(self, postData):
        errors = []
        if not postData['name']:
            errors.append('Name field cannot be blank')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid Email format')
        if not PHONE_REGEX.match(postData['phone']):
            errors.append('Invalid Phone Number Format...(###)###-####')
        return errors
    def project_valid(self, postData):
        errors = []
        if not postData['name']:
            errors.append('Name field cannot be blank')
        return errors
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()
    pass

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="project")
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()
    pass
