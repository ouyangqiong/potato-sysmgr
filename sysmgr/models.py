# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login_name= models.CharField(max_length=30, default='')
    password = models.CharField(max_length=128, default='')
    username = models.CharField(max_length=50, default='')
    empno = models.CharField(max_length=30, default='')
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField()
    created_at = models.DateTimeField()


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30, default='')
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name="parent group")

    def __str__(self):
        return self.name
