from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} {self.product.name} {self.quantity}"
    
    def dicounted_total(self):
        return self.quantity * self.product.discount
    
    def original_total(self):
        return self.quantity * self.product.price