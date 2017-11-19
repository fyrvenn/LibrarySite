# -*- coding: utf-8 -*-
from django.conf.urls import url
from library.views import RegisterFormView, LoginFormView, LogoutView, search_book, update_author, authors, add_author, update_author_func, delete_author, books, add_book, update_book, update_book_func, delete_book

urlpatterns = [
 url(r'^$', books, name='books'),
 url(r'^authors', authors, name='authors'),
 url(r'^add_author', add_author, name='add_author'),
 url(r'^update_author', update_author, name='update_author'),
 url(r'^(?P<id>[0-9]+)/update_author/$', update_author_func, name='update_author_func'),
 url(r'^delete_author', delete_author, name='delete_author'),
 url(r'^books', books, name='books'),
 url(r'^add_book', add_book, name='add_book'),
 url(r'^update_book', update_book, name='update_book'),
 url(r'^(?P<id>[0-9]+)/update_book/$', update_book_func, name='update_book_func'),
 url(r'^delete_book', delete_book, name='delete_book'),
 url(r'^search_book', search_book, name='search_book'),
 url(r'^register/$', RegisterFormView.as_view(), name='register'),
 url(r'^login/$', LoginFormView.as_view(), name='login'),
 url(r'^logout/$', LogoutView.as_view(), name='logout'),
]