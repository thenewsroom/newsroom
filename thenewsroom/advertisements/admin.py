# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Advertisement, Advertiserdetails

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',  'created_by',
                    'comments',)
    list_filter = ( 'active',)
    search_fields = ['name', ]
    fieldsets = ((None, {
        'fields': (('name', 'comments', 'active',), ('link', 'image',), ( 'created_by'),
                   )
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100

    #inlines = [OrderedProductInline]
    #readonly_fields = ('created_on',)
admin.site.register(Advertisement, AdvertisementAdmin)

class AdvertiserdetailsAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'email', 'plan', 'active', 'status','comments',)
    list_filter = ('active', 'status')
    search_fields = ['name', 'email', 'mobile']
    fieldsets = ((None, {
        'fields': (('mobile', 'advertisement', 'name',), ('email', 'comments', 'active',),
                   ('payment_due', 'plan', 'payed_on', 'payment_received_amount', 'total_payment', 'status'))
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100
    readonly_fields = ('payment_due',)
# Register your models here.

admin.site.register(Advertiserdetails, AdvertiserdetailsAdmin)
