from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=28)

class Tag(models.Model):
    name = models.CharField(max_length=28)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveIntegerField()
    Category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.name}, price {self.price} {self.stock}"

class Subscription(models.Model):
    name = models.CharField(max_length=30)

class Customer(models.Model):
    Subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)