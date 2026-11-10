"""Sample data. Safe to run more than once: it uses get_or_create.

Run from the project folder:
    docker compose exec -T web python manage.py shell < catalog/seed.py
"""
from datetime import date

from catalog.models import Author, Book, Genre, Languages

english, _ = Languages.objects.get_or_create(
    code="en", defaults={"name": "English"})
italian, _ = Languages.objects.get_or_create(
    code="it", defaults={"name": "Italian"})

scifi, _ = Genre.objects.get_or_create(name="Science Fiction")
fantasy, _ = Genre.objects.get_or_create(name="Fantasy")
classic, _ = Genre.objects.get_or_create(name="Classic")

herbert, _ = Author.objects.get_or_create(
    first_name="Frank", last_name="Herbert",
    defaults={"birth_date": date(1920, 10, 8),
              "death_date": date(1986, 2, 11)},
)
gibson, _ = Author.objects.get_or_create(
    first_name="William", last_name="Gibson",
    defaults={"birth_date": date(1948, 3, 17)},
)
tolkien, _ = Author.objects.get_or_create(
    first_name="J. R. R.", last_name="Tolkien",
    defaults={"birth_date": date(1892, 1, 3), "death_date": date(1973, 9, 2)},
)
austen, _ = Author.objects.get_or_create(
    first_name="Jane", last_name="Austen",
    defaults={"birth_date": date(1775, 12, 16),
              "death_date": date(1817, 7, 18)},
)

# python manage.py shell < catalog/seed.py


books = [
    # isbn, title, year, pages, available, language, authors, genres, summary
    ("9780441013593", "Dune", None, 612, True, english, [herbert], [scifi],
     "A noble family takes control of a desert planet and its precious spice."),
    ("9780441569595", "Neuromancer", None, 271, False, english, [gibson], [scifi],
     "A washed-up hacker is hired for one last job in cyberspace."),
    ("9780345339683", "The Hobbit", None, 310, True, english, [tolkien], [fantasy],
     "A hobbit joins a company of dwarves to reclaim a stolen treasure."),
    ("9780141439518", "Pride and Prejudice", None, 432, True, english, [austen], [classic],
     ""),  # empty summary on purpose: good for testing the default filter
]

for isbn, title, year, pages, available, language, authors, genres, summary in books:
    book, created = Book.objects.get_or_create(
        isbn=isbn,
        defaults={
            "title": title,
            "publication_date": year,
            "pages": pages,
            "available": available,
            "language": language,
            "summary": summary,
        },
    )
    if created:
        book.authors.set(authors)  # M2M links need a saved book
        book.genres.set(genres)

print(f"Books in database: {Book.objects.count()}")
