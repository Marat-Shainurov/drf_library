from django.db import models

from library.validators import ISBNValidator, PublishYearValidator


class Book(models.Model):
    isbn_validator = ISBNValidator()
    publish_year_validator = PublishYearValidator()

    title = models.CharField(verbose_name='title', max_length=250)
    author = models.CharField(verbose_name='author', max_length=150)
    ISBN = models.CharField(verbose_name='ISBN', max_length=17, validators=[isbn_validator])
    publish_year = models.CharField(verbose_name='publish_year', max_length=4, validators=[publish_year_validator])

    def __str__(self):
        return f'"{self.title}" {self.author}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
