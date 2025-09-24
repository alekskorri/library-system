from django.contrib import admin
from .models import Books, Genre


class AdminBooks(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'gener', 'publisher', 'price', 'create_by', 'created_date', 'update_by', 'update_date'
    ]


admin.site.register(Genre)
admin.site.register(Books, AdminBooks)
