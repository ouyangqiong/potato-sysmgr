# coding=utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=30, default='')
    desc = models.CharField(max_length=200, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
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
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6, default='')
    name = models.CharField(max_length=20, default='')
    desc = models.CharField(max_length=50, default='')
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name="parent group")
    user = models.ManyToManyField(User)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Menu(models.Model):
    MENU_TYPE = (
        ("dashboard", "dashboard"),
        ("console", "console"),
    )
    id = models.AutoField(primary_key=True)
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name="parent menu")
    code = models.CharField(max_length=6, default='')
    name = models.CharField(max_length=20, default='')
    desc = models.CharField(max_length=50, default='')
    addr = models.CharField(max_length=150, blank=True, null=True)
    addr_param = models.CharField(max_length=50, blank=True)
    i_class = models.CharField(max_length=100, null=True, blank=True)
    sort = models.IntegerField(blank=True, null=True)
    menu_type = models.CharField(max_length=20, default="console", choices=MENU_TYPE)
    is_active = models.BooleanField(default=True)

    meta = {
        "ordering": ['sort']
    }

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Provider(models.Model):
    CLOUD_TYPE = (
        ("private", "private"),
        ("private", "public"),
    )
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6, default='')
    name = models.CharField(max_length=20, default='')
    desc = models.CharField(max_length=50, default='')
    cloud_type = models.CharField(max_length=20, default="private", choices=CLOUD_TYPE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}|{1}".format(self.code, self.name)


@python_2_unicode_compatible
class Region(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6, default='')
    name = models.CharField(max_length=20, default='')
    desc = models.CharField(max_length=50, default='')
    is_active = models.BooleanField(default=True)
    provider = models.ForeignKey(Provider, to_field="id")
    menu = models.ManyToManyField(Menu, null=True, blank=True)

    def __str__(self):
        return "{0}|{1}".format(self.code,self.name)


class RoleMenuPermission(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, to_field="id")
    menu = models.ForeignKey(Menu, to_field="id")


class RoleRegionPermission(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, to_field="id")
    region = models.ForeignKey(Region, to_field="id")
