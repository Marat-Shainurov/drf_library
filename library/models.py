from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name='title', max_length=250)
    author = models.CharField(verbose_name='author', max_length=150)
    ISBN = models.CharField(verbose_name='ISBN', max_length=17)
    publish_year = models.CharField(verbose_name='publish_year', max_length=4)

    def __str__(self):
        return f'"{self.title}" {self.author}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
