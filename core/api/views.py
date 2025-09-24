from django.db.models import Q
from rest_framework.response import Response
from rest_framework import permissions
from .serialize import SerializerBooks
from ..models import Books
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    items = Books.objects.all()
    serializer = SerializerBooks(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getBook(request, id):
    items = Books.objects.get(id=id)
    serializer = SerializerBooks(items, many=False)
    return Response(serializer.data)

