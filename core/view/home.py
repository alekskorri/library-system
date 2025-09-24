from pprint import pprint

from django.db.models import Q
from django.shortcuts import render

from ..models import Books


# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello World....</h1>')

# books_data = [
#     {'id': 1, 'title': 'The name of the wind', 'author': 'Patric Rothfuss'},
#     {'id': 2, 'title': 'Castle', 'author': 'Ismail Kadare'},
#     {'id': 3, 'title': 'Hary Potter', 'author': 'Ismail '},
#     {'id': 4, 'title': 'Hary Potter', 'author': 'Ismail '},
# ]


def home(request):
    template_name = 'core/home.html'

    query = request.GET.get('q', '')

    if query:
        books_data = Books.objects.only('title', 'author', 'price').filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(price__icontains=query)
        )
        query_len = True
    else:
        books_data = Books.objects.only('title', 'author', 'price')
        query_len = False

    context = {'books': books_data, 'query_len': query_len}
    return render(request, template_name, context)
