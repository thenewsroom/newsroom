# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

PAYMENT_STATUS = (
    (1, 'Pending'),
    (2, 'clear'),
)

def company_logo(instance, filename):
    if filename:
        target_dir = 'uploads/company_img/'
        _, ext = filename.rsplit('.', 1)
        filename = str(filename) + '.' + ext
        return '/'.join([target_dir, filename])

# Create your models here.
class Advertisement(models.Model):
    name = models.CharField('Headline', max_length=400)
    created_on = models.DateTimeField('Created on', db_index=True
    )
    created_by = models.ForeignKey(User,
            related_name='createdby_user', default=1
    )
    comments = models.CharField(max_length=4000, blank=True, null=True)
    active = models.BooleanField(default=True)
    link = models.URLField(max_length=800, blank=True, null=True, db_index=True
    )
    image = models.ImageField(
        upload_to=company_logo,
        max_length=254,
        blank=True,
        null=True,
        default=''
    )
    #### add an image field to this model by refering to trademarks models syndicartion

    def __unicode__(self):
        return u'%s' %(self.name)

class Advertiserdetails(models.Model):
    advertisement = models.ForeignKey(Advertisement)
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=150)
    mobile = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    pament_due = models.FloatField(default=0.0)
    payed_on = models.DateTimeField(blank=True, null=True, db_index=True)
    payment_received_amount = models.FloatField(default=0.0)
    total_payment = models.FloatField(default=0.0)
    status = models.IntegerField(choices=PAYMENT_STATUS, default=1)

    def __unicode__(self):
        return u'%s' %(self.name)

    def save(self, *args, **kwargs):
        """" Custom save """
        if self.status == 1:
            self.pament_due = self.total_payment - self.payment_received_amount
        if self.total_payment == self.payment_received_amount:
            self.status = 2
            self.pament_due = 0.0

        super(Advertiserdetails, self).save(*args, **kwargs)