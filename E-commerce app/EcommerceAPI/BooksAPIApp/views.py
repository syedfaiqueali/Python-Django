from django.shortcuts import render
from django.contrib.auth import login
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from .models import Category, Book, Product, User, Order
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, OrderSerializer, RegisterSerializer, UserSerializer


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


class OrderViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles"""
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterAPI(generics.GenericAPIView):
    """Handle create use profiles"""
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_class = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
