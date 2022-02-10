from django.shortcuts import redirect, render
from django.urls import reverse
from books.models import Book
from datetime import datetime

def index(request):
    return redirect(reverse('books'))

def books(request):
    books = Book.objects.order_by('-pub_date').all()
    template = 'books/books_list.html'
    context = {
        'books': [
            {
                'name': book.name,
                'author': book.author,
                'pub_date': book.pub_date.isoformat()
            } for book in books
            ]
    }
    return render(request, template, context)

def books_view(request, year, month, day):
    date = f'{year}-{month}-{day}'
    books = Book.objects.filter(pub_date=date).all()
    previous_date = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()

    template = 'books/books_date.html'
    context = {
        'books': [
            {
                'name': book.name,
                'author': book.author,
                'pub_date': book.pub_date
            } for book in books
            ],
        'has_previous': previous_date.pub_date.isoformat() if previous_date else 0,
        'has_next': next_date.pub_date.isoformat() if next_date else 0
    }
    print(context)
    return render(request, template, context)
