from curses.ascii import SUB
from django.contrib import admin
from base.models import Product, Order, OrderItem, Category,ShippingAddress,Review, SubCategory, User

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)

admin.site.register(SubCategory)
# admin.site.register(SubSubCategory)
# admin.site.register(SubSubSubCategory)

admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)