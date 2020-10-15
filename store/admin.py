from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Addresses,
    Product,
    Order,
    Delivery
)

admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(Addresses)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)