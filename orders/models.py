from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
# Create your models here.

User = get_user_model()




STATUS_CHOICES = (
    ("P","Pending"),
    ("D","Deleviry",),
    ("C","Delevired",),
    ("F", "Failed")
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address = models.TextField()
    phone= models.IntegerField()
    total = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(default='P',max_length=4, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} "