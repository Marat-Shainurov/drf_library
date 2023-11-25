from django.contrib import admin
from django.contrib.admin import ModelAdmin

from library.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_year', 'ISBN')
    list_filter = ('author', 'publish_year')
    search_fields = ('id', 'title', 'ISBN')
