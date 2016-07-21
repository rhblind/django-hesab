# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Person(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthdate = models.DateField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
