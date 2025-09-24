from django.shortcuts import render, get_object_or_404, redirect
from .. models import Books
from ..forms import BooksForm
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required()
def edit_books(request, id):
    template_name = 'core/edit.html'

    obj = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            try:
                # Use atomic transaction
                with transaction.atomic():
                    book = form.save(commit=False)

                    book.update_by = request.user.username  # Assign the User object instead of the full name
                    book.update_date = timezone.now()
                    # Commit the changes to the database
                    book.save()

                messages.success(request, 'The record is updated successfully')
                return redirect('home')
            except Exception as e:
                # Handle exceptions and rollback the transaction if something goes wrong
                messages.error(request, f'Failed to update: {str(e)}')
        else:
            messages.error(request, 'Failed to update...')

    else:
        form = BooksForm(instance=obj)

    context = {'form': form}
    return render(request, template_name, context)
