from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct, UserViewSet, OrderViewSet


router = DefaultRouter()
router.register('profile', UserViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('', include(router.urls)),
]
