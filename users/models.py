from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    phone= models.IntegerField(null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"