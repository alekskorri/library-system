from django.urls import path
from .views import getRoutes, getBook

urlpatterns = [
    path('', getRoutes),
    path('book/<str:id>/', getBook),

]
