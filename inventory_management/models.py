from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.description}"


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    stock_movements = models.ManyToManyField(StockMovement)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
