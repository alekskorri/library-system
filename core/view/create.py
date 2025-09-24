from django.shortcuts import render, redirect
from ..forms import BooksForm
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required()
def create(request):
    template_name = 'core/create.html'

    if request.method == 'POST':
        form_book = BooksForm(request.POST, request.FILES)
        if form_book.is_valid():
            try:
                with transaction.atomic():
                    create_book = form_book.save(commit=False)

                    create_book.create_by = request.user.username
                    create_book.created_date = timezone.now()

                    create_book.save()

                    messages.success(request, 'The Book is created successfully')
                    return redirect('home')
            except Exception as e:
                # Handle exceptions and rollback the transaction if something goes wrong
                messages.error(request, f'Failed to update: {str(e)}')
        else:
            messages.error(request, 'Error during create the object')

    else:
        form_book = BooksForm

    context = {'form': form_book}

    return render(request, template_name, context)