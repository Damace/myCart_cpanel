from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    supplier_phone = models.CharField(max_length=15)
    supplier_address = models.TextField()

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('All', 'All'),
        ('Women', 'Women'),
        ('Men', 'Men'),
        ('Kids', 'Kids'),
        ('Sports', 'Sports'),
        ('Formal', 'Formal'),
        ('Gadgets', 'Gadgets'),
        ('Clothing', 'Clothing'),
        ('Fashion', 'Fashion'),
        ('Electronics', 'electronics'),
        ('Stationeries', 'Stationeries'),
        ('Gender_gadgets', 'Gender_gadgets'),
        ('Kitchenware', 'Kitchenware'),
        ('Home_items', 'Home items'),
        ('Featured', 'Featured'),   
        ('Games', 'Games'),
        ('Books', 'Books'),
        ('Accessories', 'Accessories'),
        ('Handbags', 'Handbags'),
        ('Oils', 'Oils'),
        ('Other', 'Other'),
    ]
  
    CLOTH_CATEGORY_CHOICES = [
        ('Empty', 'Empty'),
        ('Men_clothing', 'Men Clothing'),
        ('Women_clothing', 'Women Clothing'),
        ('Kids_clothing', 'Kids Clothing'),
        ('Sports_activewear', 'Sports & Activewear'),
        ('Formal_workwear', 'Formal & Workwear'),
        ('Gadgets', 'Gadgets'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='all')
    cloth_category = models.CharField(max_length=20, choices=CLOTH_CATEGORY_CHOICES, default='empty' )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='product_images/', blank=False)
    image2 = models.ImageField(upload_to='product_images/', blank=False, null=True)  # Additional image field 2
    image3 = models.ImageField(upload_to='product_images/', blank=False, null=True)  # Additional image field 3
    description = models.TextField(blank=False)
    price = models.PositiveIntegerField(default=0)
    unitTag = models.SlugField(max_length=100,default=0,editable=False)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    rates = models.DecimalField(max_digits=3,decimal_places=2,default=0.0,help_text="Average rating from 0.0 to 5.0")
    orders = models.PositiveIntegerField(default=0)  # Number of orders for the product
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            self.unitTag = slugify(f"{self.price}")
        super().save(*args, **kwargs)



from django.db import models
from django.utils.timezone import now

class ProductReview(models.Model):
    product_name = models.CharField(max_length=255)  # Name of the product being reviewed
    customer = models.CharField(max_length=255)  # Name of the customer
    rates = models.FloatField(default=0.0)
    comments = models.TextField(blank=True)  # Customer's comments on the product
    comments_date = models.DateTimeField(default=now)  # Date and time the comment was made

    def __str__(self):
        return f"{self.product_name} - {self.customer}"

