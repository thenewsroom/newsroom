# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'status',  'published_date',)
    list_filter = ('created_on', 'status', 'category', 'subcategory', 'published_date', 'story_status')
    search_fields = ['title', ]
    fieldsets = ((None, {
        'fields': (('title', 'slug', 'sub_headline',), ('status', 'body_html', 'published_date',), ('created_on', 'created_by'),
                   ('subcategory', 'publication', 'category',), ('image', 'updated_on', 'published_by','story_status',),
                   ('url', 'author', 'approved_on','approved_by', 'comments', 'credit_line',))
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100

    #inlines = [OrderedProductInline]
    readonly_fields = ('updated_on', 'created_on',)
admin.site.register(Content, ContentAdmin)

# Register your models here.
