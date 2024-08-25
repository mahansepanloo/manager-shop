from django.contrib import admin
from .models import Product,Category,Comment,Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass



@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('total_rate','name','price')

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass