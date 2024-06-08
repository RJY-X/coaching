from django.contrib import admin
from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderToProduct,
    ProductImages,
    ProductVariant,
)
# Register your models here.

admin.site.register(Product)

admin.site.site_header='APOSTEl PANEL'
admin.site.site_title='APOSTEl PANEL'

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(ProductImages)
admin.site.register(ProductVariant)

