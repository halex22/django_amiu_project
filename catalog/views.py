from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from catalog.models import Book
# Create your views here.


def get_books(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'book_list.html', context={"books": books})


def get_book_details(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(id=pk)
    return render(request, 'book_details.html', context={"book": book})
