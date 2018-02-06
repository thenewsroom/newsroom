# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from publications.models import Publication

from category.models import Category, SubCategory

from django.contrib.auth.models import User


PUB_STATUS = (
    (-1, 'Rejected'),
    (0, 'Draft'),
    (1, 'Pending Review'),
    (2, 'Published'),
)

STORY_STATUS = (
    (0, 'None'),
    (1, 'Word Count'),
    (2, 'Duplicate'),
    (3, 'Merged Words'),
)

def story_image(instance, filename):
    if filename:
        target_dir = 'uploads/story_image/'
        fname, ext = filename.rsplit('.', 1)
        filename = str(fname) + '.' + ext
        return '/'.join([target_dir, filename])

# Create your models here.
class Content(models.Model):
    title = models.CharField('Headline', max_length=400)
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(SubCategory,blank=True, null=True)
    sub_headline = models.CharField(
        'Secondary headline (optional)', max_length=255, blank=True
    )
    slug = models.SlugField(
        max_length=350,
        # unique_for_date='pub_date',
        help_text='Automatically built from the title.'
    )
    image = models.ImageField(
        upload_to=story_image,
        max_length=254,
        blank=True,
        null=True,
        default=''
    )
    status = models.IntegerField(choices=PUB_STATUS, default=0)
    body_html = models.TextField(blank=True)
    published_date = models.DateTimeField('Date published', db_index=True)

    publication = models.ForeignKey(
        Publication, limit_choices_to={'active': True}
    )
    credit_line = models.CharField(
        max_length=255, blank=True,
        help_text="Leave it blank for it to be populated by the system."
    )
    top_pick = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(
        'Created on', auto_now_add=True, db_index=True
    )
    story_status = models.IntegerField(
        choices=STORY_STATUS, default=0
    )
    created_by = models.ForeignKey(
        User, limit_choices_to={'is_staff': True, 'is_active': True},
        related_name='entries', default=1
    )
    published_by = models.ForeignKey(
        User, limit_choices_to={'is_staff': True, 'is_active': True},
        related_name='Content_ser', blank=True, null=True
    )
    url = models.URLField(
        max_length=800, blank=True, db_index=True
    )
    author = models.CharField(max_length=200, blank=True)
    approved_on = models.DateTimeField(blank=True, null=True, db_index=True)
    approved_by = models.ForeignKey(
        User, limit_choices_to={'is_staff': True, 'is_active': True},
        related_name='approved_contents', blank=True, null=True
    )
    comments = models.CharField(max_length=400,blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        ordering = ('-published_date',)

    def save(self, *args, **kwargs):
        """"
        Custom
        save
        """
        if not self.slug:
            self.slug = self.title.lower().replace(' ', '-')

        super(Content, self).save(*args, **kwargs)

