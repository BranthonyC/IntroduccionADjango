from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from books.models import Book
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "bookstore/list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "bookstore/detail.html"
    context_object_name = "book"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "bookstore/delete.html"
    context_object_name = "book"
    success_url = "/"
