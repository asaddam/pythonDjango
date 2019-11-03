# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Roles (models.Model):
    role = models.fields.CharField(max_length=255)

    class Meta:
        verbone_name_plural = 'roles'

    def __str__(self):
        return self.role

    def __str__(self):
        return self.role

class Goals (models.Model):
    Goals = models.foreignKey(Roles, on_delete=models.CASCADE())