from django.contrib import admin

from book.models.author import Author
from book.models.book import Book
from book.models.category import Category
from book.models.request import Request
from book.models.user_book import UserBook

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Request)
admin.site.register(UserBook)
