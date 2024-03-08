from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()
