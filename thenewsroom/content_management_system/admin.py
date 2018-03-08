# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Content, ContentLoadStatus, Video
from django import forms
from .forms import ContentAdminForm
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from tinymce.widgets import AdminTinyMCE


class TrendingFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('trending')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'trending_filter'

    def lookups(self, request, model_admin):
        return (
            ('trending', _('trending')),
            ('not_miss', _('not_miss')),
            ('top_pick', _('top_pick'))
        )

    def queryset(self, request, queryset):
        if self.value()== 'trending':
            return queryset.filter(trending=True)
        elif self.value()== 'not_miss':
            return queryset.filter(not_miss=True)
        elif self.value()== 'top_pick':
            return queryset.filter(top_pick=True)
        else:
            return queryset

class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    list_display = ('title', 'publication', 'status',  'published_date',)
    list_filter = ('created_on', TrendingFilter, 'status', 'category', 'subcategory', 'published_date', 'story_status')
    search_fields = ['title', ]
    prepopulated_fields = {"slug": ('title',)}
    fieldsets = ((None, {
        'fields': (('title', 'slug', 'sub_headline',), ('status', 'body_html', 'top_pick', 'trending', 'not_miss', 'published_date',), ('created_on', 'created_by'),
                   ('subcategory', 'publication', 'category',), ('image', 'updated_on',), ('published_by','story_status',),
                   ('url', 'author', 'approved_on',),
                   ('approved_by', 'comments', 'credit_line',),('story_image1', 'story_image2', 'story_image3','story_image4'))
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100

    #inlines = [OrderedProductInline]
    readonly_fields = ('updated_on', 'created_on',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        # use TinyMCE widget for body_html
        if db_field.name == 'body_html':
            kwargs['widget'] = AdminTinyMCE
        return super(ContentAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.status in [2,-1]:
            if obj.status == 2:
                obj.published_by = request.user
            obj.approved_on = datetime.now()
            obj.approved_by = request.user
        obj.updated_on = datetime.now()
        super(ContentAdmin, self).save_model(request, obj, form, change)
admin.site.register(Content, ContentAdmin)

class ContentLoadStatusAdmin(admin.ModelAdmin):
    list_display = ('filename', 'status', 'comments', 'created_on',)
    list_filter = ('created_on', 'status',)
    fieldsets = ((None, {
        'fields': (('filename', 'status', 'comments', 'created_on',))
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100

    # inlines = [OrderedProductInline]
    readonly_fields = ('comments','created_on',)
admin.site.register(ContentLoadStatus, ContentLoadStatusAdmin)
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_on',)
    list_filter = ('created_on', 'active',)
    fieldsets = ((None, {
        'fields': (('name', 'active', 'image', 'link', 'created_on', 'created_by',))
    }
                  ),
                 )
    # list_editable = ('status',)
    ist_per_page = 100

    # inlines = [OrderedProductInline]
    #readonly_fields = ('comments','created_on',)
admin.site.register(Video, VideoAdmin)