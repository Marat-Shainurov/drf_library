from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class BookAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email', 'registration_date')
    search_fields = ('id', 'username', 'email')
