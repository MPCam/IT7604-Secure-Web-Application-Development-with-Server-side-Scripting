from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Borrower, Loan
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'books/author_list.html'

class BorrowerDetailView(LoginRequiredMixin,generic.DetailView):
    model = Borrower
    template_name = 'books/borrower_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan_count'] = Loan.objects.filter(borrower = self.object).count()
        context['loaned_books'] = Loan.objects.filter(borrower = self.object)
        return context
    
class AuthorsWithBooksView(generic.ListView):
    model = Author
    template_name = 'books/author_with_books.html'

    def get_queryset(self):
        return Author.objects.annotate(book_count=Count('book')).filter(book_count__gte = 1)
    
class AuthorDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Author
    template_name = 'books/author_detail.html'

    def test_func(self):
        author = self.get_object()
        return (
            self.request.user.groups.filter(name='Authors').exists()
            and author.user == self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object)
        return context
    
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loans'] = Loan.objects.filter(book=self.object)
        return context
    
class UnusedBooksView(generic.ListView):
    model = Book
    template_name = 'books/unused_books.html'

    def get_queryset(self):
        return Book.objects.annotate(loan_count = Count('loan')).filter(loan_count = 0)
    
class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields='__all__'
    template_name = 'books/book_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('book_list')
    
class BookEditView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields='__all__'
    template_name= 'books/book_form.html'
    def test_func(self):
        book = self.get_object()
        return book.author.user == self.request.user
    def get_success_url(self):
        return reverse_lazy('book_list')
    
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name= 'books/book_delete.html'
    def test_func(self):
        book = self.get_object()
        return book.author.user == self.request.user
    def get_success_url(self):
        return reverse_lazy('book_list')

class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    fields='__all__'
    template_name = 'books/author_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('author_list')
    
class AuthorEditView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Author
    fields='__all__'
    template_name= 'books/author_form.html'
    def test_func(self):
        author = self.get_object()
        return author.user == self.request.user
    def get_success_url(self):
        return reverse_lazy('author_list')
    
class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Author
    template_name= 'books/author_delete.html'
    def test_func(self):
        author = self.get_object()
        return author.user == self.request.user
    def get_success_url(self):
        return reverse_lazy('author_list')