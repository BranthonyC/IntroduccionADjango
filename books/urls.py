from django.urls import path
from books.views import BookListView, BookDetailView, BookDeleteView


urlpatterns = [
    path('', BookListView.as_view(), name="books_list"),
    path('detail/<int:pk>', BookDetailView.as_view(), name="book_detail"),
    path('delete/<int:pk>', BookDeleteView.as_view(), name="book_delete"),
]
