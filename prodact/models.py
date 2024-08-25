from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='product_name',
                            help_text='product name should be less than 100 characters', null=True, blank=True)
    description = models.TextField(verbose_name='product_description',
                                   help_text='a simple description about the product', null=True, blank=True)
    price = models.FloatField(verbose_name='product_price', null=True, blank=True)
    stock = models.IntegerField(verbose_name='product_stock', help_text='products stock should be a natural number',
                                null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)





    def total_rate(self):
        sumrate =  (sum(item.get_rate() for item in self.frate.all()))
        if sumrate != 0:
            countrata = sumrate / self.frate.count()
            return countrata
        else:
            return None


    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='category_name',
                            help_text='category name should be less than 50 characters', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Comment(models.Model):
    comment_text = models.TextField(verbose_name='comment', null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_text


class Rate(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    rater = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='frate')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def get_rate(self):
        return self.rating

    def __str__(self) -> str:
        return f"{self.rating}, {self.rater}"