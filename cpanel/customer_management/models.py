from django.db import models
from product_management.models import Product

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name}'
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Processed', 'Processed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ])

    def __str__(self):
        return f"Order {self.id} - {self.customer}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('product_management.Product', on_delete=models.CASCADE, related_name='customer_order_items')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"