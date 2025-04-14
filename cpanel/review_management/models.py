from django.db import models
from django.utils.text import slugify

# Import the `Customer` model (update with the actual path to your `Customer` model)
from customer_management.models import Customer  # Adjust the path as needed
from product_management.models import Product  # Assuming you have a Product model in product_management

from django.db import models
from product_management.models import Product
from customer_management.models import Customer  # Use your actual import path for Customer

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)  # Use Customer model instead of User
    rating = models.PositiveIntegerField()  # Rating out of 5
    comment = models.TextField(blank=True)  # Optional comment
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        # Use `full_name` attribute of `Customer`
        return f'Review by {self.user.full_name} on {self.product.name}'
