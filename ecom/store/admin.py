from django.contrib import admin
from .models import Category,Customer,Product,Order,Address,Request,Manager,Chat
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Request)
admin.site.register(Manager)
admin.site.register(Chat)

# class Product_admin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('p_name',)}