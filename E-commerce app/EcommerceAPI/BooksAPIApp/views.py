from django.shortcuts import render
from rest_framework import generics

from .models import Category, Book, Product
from .serializers import CategorySerializer, BookSerializer, ProductSerializer


# Create your views here.
class ListCategory(generics.ListCreateAPIView):
    """ View for List """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    """ View for Detail Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListBook(generics.ListCreateAPIView):
    """ View for Detail Book List """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    """ View for Book Detail"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListProduct(generics.ListCreateAPIView):
    """ View for Detail Product List """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    """ View for Product Detail"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
