from django.contrib import admin

from catalog.models import Author, Book, Genre, Languages

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ...


@admin.register(Languages)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "code"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...
