# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from category.models import Category

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(
        'Created on', db_index=True
    )
    updated_on = models.DateTimeField()
    copyright = models.CharField(max_length=255, null=True, blank=True,
                                 help_text="Leave blank to pick the default account level settings, \
                                 for Custom say: Custom Copyright for issued by")
    auto_schedule = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' %(self.title)

    def save(self, *args, **kwargs):
        """" Custom save """
        if not self.slug:
            self.slug = self.title.lower().replace(' ', '-')

        super(Publication, self).save(*args, **kwargs)

# class RssFeed(models.Model):
#     name = models.CharField(max_length=400)
#     url = models.URLField(
#         max_length=800, blank=True, db_index=True
#     )
#     created_on = models.DateTimeField(
#         'Created on', db_index=True
#     )
#     comments = models.CharField(max_length=400, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     category = models.ForeignKey(Category)
#
#     class Meta:
#         verbose_name_plural = "Rss Feeds"
#
#     def __unicode__(self):
#         return u'%s-%s' % (self.name, self.url)

