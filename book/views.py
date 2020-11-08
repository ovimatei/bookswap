from django.shortcuts import render
from .models.book import Book


def home(request):
    context = {
        "books": Book.objects.all(),
    }

    return render(request, template_name='home.html', context=context)
