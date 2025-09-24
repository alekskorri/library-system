from django.urls import path
from .view.home import home
from .view.detail import detail, view
from .view.edit import edit_books
from .view.delete import delete
from .view.create import create
from .view.genre_filter import genre_filter


urlpatterns = [
    path('', home, name='home'),
    path('view/', view, name='view'),
    path('create/', create, name='create'),
    path('detail/<id>', detail, name='detail'),
    path('edit/<id>', edit_books, name='edit_books'),
    path('delete/<id>', delete, name='delete'),

    path('genre_filter/<name>', genre_filter, name='genre_filter'),


]
