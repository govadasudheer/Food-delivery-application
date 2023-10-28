from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='foodorder/static/images/')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    