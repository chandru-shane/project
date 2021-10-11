from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128)
    product_image = models.ImageField(upload_to='products')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name