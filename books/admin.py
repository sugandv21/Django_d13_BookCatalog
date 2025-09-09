from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","genre","published_date")
    search_fields = ("title","author","genre")
    list_filter = ("genre","published_date")
    ordering = ("-created_at",)
