from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('borrower/<int:pk>/', views.BorrowerDetailView.as_view(), name='borrower_detail'),
    path('authors/active', views.AuthorsWithBooksView.as_view(), name='authors_with_books'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('unused_books/', views.UnusedBooksView.as_view(), name='unused_books'),
    path('book/add/', views.BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/edit/', views.BookEditView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author_add'),
    path('author/<int:pk>/edit/', views.AuthorEditView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]