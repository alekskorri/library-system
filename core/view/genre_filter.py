from django.db.models import Q
from django.shortcuts import render
from ..models import Books


def genre_filter(request, name):
    template_name = 'core/genre_filter.html'

    if request:
        books_data = Books.objects.only('title', 'author', 'price').filter(
            Q(gener__genre__icontains=name)

        )
        query_len = True
    else:
        query_len = False

    context = {'books': books_data, 'query_len': query_len}

    return render(request, template_name, context)
