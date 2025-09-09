from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from django.db.models import Q
from .models import Book

def books_list(request):
    q = request.GET.get('q', '').strip()
    if q:
        books = Book.objects.filter(Q(title__icontains=q) | Q(genre__icontains=q)).order_by('-created_at')
    else:
        books = Book.objects.all().order_by('-created_at')

    return render(request, "books/books_list.html", {"books": books, "q": q})


# DRF ViewSet with search by title and genre
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre']  



