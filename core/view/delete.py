from django.shortcuts import render, get_object_or_404, redirect
from .. models import Books
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def delete(request, id):
    template_name = 'core/delete.html'
    obj = get_object_or_404(Books, id=id)

    if request.method == 'POST':
        if obj:
            obj.delete()
            messages.success(request, 'This record was deleted successfully')
            return redirect('home')
        else:
            messages.error(request, "Failed to delete...")

    return render(request, template_name)
