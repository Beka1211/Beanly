from django.db import models
class Brand(models.Model):
    title = models.CharField(max_length=100)

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Storage(models.Model):
    stock = models.IntegerField()

    def __str__(self):
        return self.stock

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
