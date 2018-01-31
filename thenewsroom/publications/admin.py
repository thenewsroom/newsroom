# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Publication

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
# Register your models here.
