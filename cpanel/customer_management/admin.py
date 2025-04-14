from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number','email','address','city', 'country','postal_code','password']
    search_fields = ['full_name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_date','status']
    search_fields = ['customer']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','quantity']
    search_fields = ['order']

admin.site.register(Order, OrderAdmin)
admin.site.register( OrderItem,  OrderItemAdmin)
admin.site.register(Customer, CustomerAdmin)
