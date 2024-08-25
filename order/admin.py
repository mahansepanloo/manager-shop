from django.contrib import admin
from .models import Order,OrderItem

class Order_itemadmin(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class OrderItemAdmin(admin.ModelAdmin):
    inlines = (Order_itemadmin,)

