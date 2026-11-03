from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(TimeStampModel):
    name = models.CharField(max_length=100, unique=True, null=False)
    # valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'genres'
        ordering = ["name"]
        # managed= False

    def __str__(self):
        return self.name


class Languages(TimeStampModel):
    name = models.CharField(max_length=50, unique=True, null=False)
    code = models.CharField(max_length=2, unique=True, null=False)

    class Meta:
        db_table = 'languages'
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(TimeStampModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)

    class Meta:
        db_table = "authors"
        ordering = ["last_name", "first_name"]
        indexes = [
            models.Index(fields=["last_name", "first_name"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["last_name", "first_name"],
                name="unique_author_identity"
            )
        ]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Book(TimeStampModel):
    title = models.CharField(max_length=250, null=False)
    summary = models.TextField(null=True)
    isbn = models.CharField(
        max_length=13,
        null=False,
        validators=[RegexValidator(
            r"^\d{13}$", "ISBN must be exactly 13 digits")]
    )
    publication_date = models.DateField(null=True)
    pages = models.PositiveIntegerField(
        null=True,
        validators=[
            MinValueValidator(20, "boo must have at least 20 pages"),
            MaxValueValidator(5_000, "book must have max 5 000 pages")
        ]
    )

    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    language = models.ForeignKey(
        Languages, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.title
