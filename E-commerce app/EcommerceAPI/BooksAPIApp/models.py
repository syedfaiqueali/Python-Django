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
