from rest_framework import serializers
from .models import Category, Book, Product


class CategorySerializer(serializers.ModelSerializer):
    """Serializes a Category object"""

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )


class BookSerializer(serializers.ModelSerializer):
    """Serializes a Book object"""

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'
        )


class ProductSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""

    class Meta:
        model = Product
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created'
        )
