from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models.book import Book
from .models.user_book import UserBook


def about(request):
    return render(request, template_name='about.html')


def user_profile(request):
    user_books = UserBook.objects.filter(user_id=request.user.id)

    return render(request, 'profile.html', {"user_books": user_books})


class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book.html'


class BookAddView(CreateView):
    model = Book
    template_name = 'add_book.html'
    success_url = reverse_lazy('user_profile')
    fields = "__all__"
