from django.db import models
from django.contrib.auth.models import User

# Farmer / Buyer Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_farmer = models.BooleanField(default=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


# Product Model
class Product(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


# Order Model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order {self.id}"
