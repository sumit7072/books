from django.shortcuts import render

# Create your views here.
from .models import Book
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerilization

class BookOperations(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerilization

