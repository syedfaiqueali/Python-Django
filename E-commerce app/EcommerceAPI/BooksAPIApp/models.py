from django.db import models


# Create your models here.
class Category(models.Model):
    """Database model for categories in system"""
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories' #For name correction in admin panel

    def __str__(self):
        return self.title


class Book(models.Model):
    """Database model for categories in system"""
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        related_name='books',
        on_delete=models.CASCADE #When category delete so all its books also delete
    )
    author = models.CharField(max_length=100, default='Anonymous')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    """Database model for products in system"""
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE #When category delete so all its products also delete
    )
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.product_tag} {self.name}'


class User(models.Model):
    """Database model for users in system"""
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Database model for orders in system"""
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order_id:{self.order_id}, User:{self.user}, Product:{self.product}, Date:{self.date_created}'
