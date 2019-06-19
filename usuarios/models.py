# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Usuarios(models.Model):
    user = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    id_number = models.CharField(max_length=255, default='')
    picture = models.ImageField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('name',)

class Tableros(models.Model):
    table_owner = models.ForeignKey(Usuarios, models.CASCADE)
    table_name = models.CharField(max_length=255, blank=True, default='')
    table_privacy = models.IntegerField()

    class Meta:
        ordering = ('table_name',)

class Ideas(models.Model):
    user_name = models.ForeignKey(Usuarios, models.CASCADE)
    table_name = models.ForeignKey(Tableros, models.CASCADE)
    thing = models.CharField(max_length=1000, default='')

    class Meta:
        ordering = ('thing',)


