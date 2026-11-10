from django.urls import path
from catalog.views import get_books, get_book_details

urlpatterns = [
    path('', view=get_books, name='book-list'),
    path('<int:pk>', view=get_book_details, name="book-detail")
]
