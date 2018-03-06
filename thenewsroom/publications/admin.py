# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Publication,RssFeed

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','active',)
    #list_editable = ('auto_schedule', )
    search_fields = ['title']
    list_filter = ('auto_schedule', 'active',)
    prepopulated_fields = {"slug": ('title', )}
    fieldsets = ((None, {'fields': (('title', 'slug',), ('description',),
                                    ('copyright','created_on','updated_on',),
                                    ('auto_schedule', 'active')
                                    )
                         }
                  ),
                 )
admin.site.register(Publication, PublicationAdmin)

class RssFeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','active','url',)
    search_fields = ['name',]
    list_filter = ('active','category',)
    fieldsets = ((None, {'fields': (('name', 'category',), ('url',),
                                    ('created_on','comments','active',),
                                    )
                         }
                  ),
                 )
admin.site.register(RssFeed, RssFeedAdmin)
# Register your models here.
