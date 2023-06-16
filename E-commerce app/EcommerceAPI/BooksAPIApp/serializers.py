from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, Book, Product, Order


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

class OrderSerializer(serializers.ModelSerializer):
    """Serializes a Order object"""

    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'product',
            'date_created'
        )


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User object"""

    class Meta:
        model = User
        fields = ('id','username','email')


class RegisterSerializer(serializers.ModelSerializer):
    """Serializes a User object"""

    class Meta:
        model = User
        fields = ('id','username','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user
