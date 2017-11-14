# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class ContactDetails(models.Model):
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250)
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ':' + self.email

class Articles(models.Model):
    status = models.CharField(max_length=1)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'created_by')
    update_user = models.ForeignKey(User, null=True, blank=True)
    image = models.CharField(max_length=50)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    on_article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)