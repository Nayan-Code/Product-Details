from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    popularity_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
