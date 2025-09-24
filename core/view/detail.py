from django.shortcuts import render, get_object_or_404
from .. models import Books


def view(request):
    template_name = 'core/view.html'

    return render(request, template_name)

def detail(request, id):
    template_name = 'core/view.html'
    obj = get_object_or_404(Books, id=id)

    context = {'book': obj}
    return render(request, template_name, context)