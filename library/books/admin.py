from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'reading_status', 'added_date']
    list_filter = ['reading_status', 'added_date']
    search_fields = ['title', 'author']
