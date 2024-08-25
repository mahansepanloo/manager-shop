from django.db import models
from django.contrib.auth.models import User
from prodact.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    delivery_cost = models.IntegerField(null=True, blank=True)


    def total_price(self):
        return sum([order.total_price() for order in self.oorderitem.all()])

    def all_product(self):
        return [(item.get_name(),item.get_num()) for item in self.oorderitem.all()]




    def __str__(self) -> str:
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='oorderitem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    num = models.IntegerField()

    def total_price(self):
        return self.price * self.num
    def get_num(self):
        return self.num
    def get_name(self):
        return self.product.name



