# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Book

#class LibraryAdmin(admin.ModelAdmin):
#    list_display = ('book_name', 'author_name')

admin.site.register(Author)
admin.site.register(Book)