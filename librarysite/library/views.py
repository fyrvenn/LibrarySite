# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Author, Book
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

def authors(request):
    authors = Author.objects.order_by('author_name')
    return render(request, 'authors.html', {
            'authors': authors,
        })
@login_required
def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        result = Author(author_name=name)
        result.save()
        return HttpResponseRedirect(reverse('authors'))
    return render(request, 'add_author.html', {
        })
@login_required
def update_author(request):
    authors = Author.objects.order_by('author_name')
    if request.method == 'POST':
        id = request.POST['id']
        author = Author.objects.get(id=id)
        return render(request, 'update_author_fields.html', {
                'author': author,
            })
    return render(request, 'update_author.html', {
            'authors': authors,
        })
@login_required
def update_author_func(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        Author.objects.filter(id=id).update(author_name=name)
        return HttpResponseRedirect(reverse('authors'))
@login_required
def delete_author(request):
    authors = Author.objects.order_by('author_name')
    if request.method == 'POST':
        id = request.POST['id']
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect(reverse('authors'))
    return render(request, 'delete_author.html', {
            'authors': authors,
        })

def books(request):
    books = Book.objects.order_by('book_name')
    return render(request, 'books.html', {
            'books': books,
        })
@login_required
def add_book(request):
    authors = Author.objects.order_by('author_name')
    if request.method == 'POST':
        name = request.POST['name']
        author_name = Author.objects.get(pk=(request.POST['author_name']))
        result = Book(book_name=name, author=author_name)
        result.save()
        return HttpResponseRedirect(reverse('books'))
    return render(request, 'add_book.html', {
            'authors': authors,
        })

def search_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        type = request.POST['search_type']
        if type == 'book':
             books = Book.objects.filter(book_name__icontains=name)
        elif type == 'author':
            authors = Author.objects.filter(author_name__icontains=name)
            books = Book.objects.filter(author__in=authors)
        return render(request, 'search_book_result.html', {
                'books': books,
                'name': name,
                'type': type,
            })
    return render(request, 'search_book.html', {
        })
@login_required
def update_book(request):
    books = Book.objects.order_by('book_name')
    if request.method == 'POST':
        id = request.POST['id']
        book = Book.objects.get(id=id)
        authors = Author.objects.order_by('author_name')
        return render(request, 'update_book_fields.html', {
                'book': book,
                'authors': authors,
            })
    return render(request, 'update_book.html', {
            'books': books,
        })
@login_required
def update_book_func(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        author_id = request.POST['author']
        author = Author.objects.get(id=author_id)
        Book.objects.filter(id=id).update(book_name=name,author=author)
        return HttpResponseRedirect(reverse('books'))
@login_required
def delete_book(request):
    books = Book.objects.order_by('book_name')
    if request.method == 'POST':
        id = request.POST['id']
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect(reverse('books'))
    return render(request, 'delete_book.html', {
            'books': books,
        })