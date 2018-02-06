# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, SubCategory, Language, TrendingCategory

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'active',)
    search_fields = ['name']
    list_filter = ('active', 'created_on',)
    prepopulated_fields = {"slug": ('name',)}
    fieldsets = ((None, {'fields': (('name', 'slug', 'active', 'created_on'),
                                    ('created_by', 'comments',),
                                    )

                         }
                  ),
                 )

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'created_on', 'active',)
    search_fields = ['name']
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ('active', 'created_on', 'category',)
    fieldsets = ((None, {'fields': (('name', 'category', 'slug', 'active', 'created_on'),
                                    ('created_by', 'comments',),
                                    )

                         }
                  ),
                 )

admin.site.register(SubCategory, SubCategoryAdmin)

class LanguageAdmin(admin.ModelAdmin):

    list_display = ('language', 'created_on', 'active',)
    search_fields = ['language']
    list_filter = ('active', 'created_on',)
    fieldsets = ((None, {'fields': (('language', 'active', 'created_on'),
                                    ('created_by', 'comments',),
                                    )

                         }
                  ),
                 )

admin.site.register(Language, LanguageAdmin)

class TrendingCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'active',)
    search_fields = ['name']
    list_filter = ('active', 'created_on',)
    prepopulated_fields = {"slug": ('name',)}
    fieldsets = ((None, {'fields': (('name', 'slug', 'active', 'created_on'),
                                    ('created_by', 'comments',),
                                    )

                         }
                  ),
                 )

admin.site.register(TrendingCategory, TrendingCategoryAdmin)
# Register your models here.
