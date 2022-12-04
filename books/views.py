from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Fantasy')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Adventure')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Romance')
    serializer_class = BookSerializer


class DystopianViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Dystopian')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Mystery')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Horror')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Thriller')
    serializer_class = BookSerializer


class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Fiction')
    serializer_class = BookSerializer


class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Children')
    serializer_class = BookSerializer


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(genre='Favorites')
    serializer_class = BookSerializer

