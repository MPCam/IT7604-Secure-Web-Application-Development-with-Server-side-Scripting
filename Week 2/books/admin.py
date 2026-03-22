from django.contrib import admin
from .models import Author, Book, Borrower, Loan

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('title', 'author__name',)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'book', 'due_date')
    search_fields = ('borrower_name', 'book_title')
    list_filter = ('due_date',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Loan, LoanAdmin)
    