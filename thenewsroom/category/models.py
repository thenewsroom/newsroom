# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(
        max_length=400,
    )
    created_on = models.DateTimeField(
        'Created on', db_index=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='user_categories', default=1
    )
    comments = models.CharField(max_length=4000,blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u'%s' % (self.name)

    def save(self, *args, **kwargs):
        """"
        Custom
        save
        """
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')

        super(Category, self).save(*args, **kwargs)

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=400)
    slug = models.SlugField(
        max_length=400,
        help_text='Automatically built from the title.'
    )
    created_on = models.DateTimeField(
        'Created on', db_index=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='scategories_user', default=1
    )
    comments = models.CharField(max_length=4000,blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __unicode__(self):
        return u'%s' % (self.name)

    def save(self, *args, **kwargs):
        """"
        Custom
        save
        """
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')

        super(SubCategory, self).save(*args, **kwargs)

class Language(models.Model):
    language = models.CharField(max_length=40)
    created_on = models.DateTimeField(
        'Created on', db_index=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='jobs', default=1
    )
    comments = models.CharField(max_length=400, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.language)

# Create your models here.
