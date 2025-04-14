from django.db import models
from django.utils.timezone import now
from clients.models import ClientProfile
from product_management.models import Product  # Adjust the app name to match your project structure



class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Not paid', 'Not paid'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.client.full_name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)  # Stores the name of the product at the time of order
    product_image = models.ImageField(upload_to='order_items/images/', blank=True, null=True)  # Stores the product image
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Unit price at the time of order

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"


class ProductOrders(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Received', 'Received'),
        ('Processing', 'Processing'),
        ('Shipping', 'Shipping'),
        ('Transporting', 'Transporting'),
        ('Rejected ', 'Rejected'),
        ('Returns', 'Returns'),
        ('Delivered', 'Delivered'),

    ]

    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    ]

    phone_number = models.CharField(max_length=15)
    product_image = models.URLField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Not Paid')
    receipt_number = models.CharField(max_length=255)
    order_date_time = models.DateTimeField(default=now)  # Automatically set to current time

    def __str__(self):
        return self.product_name




class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    receipts = models.CharField(max_length=50)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order {self.order.id}"


class ItemReview(models.Model):
    product_id = models.IntegerField()
    product_image = models.URLField()
    product_name = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    comments = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comments_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.customer} ({self.rating}★)"


class Offer(models.Model):
    product = models.ForeignKey(Product, related_name='offers', on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.discount_percentage}% off on {self.product.name}"
