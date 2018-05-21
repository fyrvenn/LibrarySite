# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = 'Авторы'

    def __unicode__(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length = 50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        verbose_name = 'Книги'

    def __unicode__(self):
        return self.book_name
